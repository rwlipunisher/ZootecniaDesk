import sqlite3
import os


class InitDataBase:

    _pathDatabase = "Resources/DataBase/main.db"

    @staticmethod
    def _openConnectDb() -> sqlite3.Connection:
        '''Utilizado para abrir a conexão com o banco de dados sqlite3'''
        try:
            connection = sqlite3.connect(InitDataBase._pathDatabase)
            return connection
        except sqlite3.Error as e:
            return e
    
    @staticmethod
    def _createDatabase() -> bool:
        '''Este método é usado apenas na ativação do software
        Observe que ele so cria o banco e a tabela do usuario
        que acessa o sistema atraves do InitDataBase._creatTableUser'''
        try:
            connection = sqlite3.connect(InitDataBase._pathDatabase)
            InitDataBase._createTableTokenAndStandardUser(connection)
            connection.close()
            return True
        except sqlite3.Error as e:      
            print(f"Erro ao criar banco de dados! Reinicie o programa: {e}")
            return False

    
    @staticmethod
    def _createTableTokenAndStandardUser(connection: sqlite3.Connection) -> bool:
        '''Este metodo é usado apenas na ativação do software
        as tabelas são criadas apenas uma vez, no processo de ativação
        e não podem ser alteradas em suas colunas e especificaçoes dos dados'''
        try:
            cursor = connection.cursor()
            # Define the SQL statements to create tables
            # Execute the SQL statements
            createTableToken = '''
            CREATE TABLE user_token_activate (
                username_access TEXT NOT NULL CHECK(LENGTH(username_access) <= 30),
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                token_activation TEXT CHECK(LENGTH(token_activation) <= 10) NOT NULL,
                password TEXT CHECK(LENGTH(password) <= 10),
                "CPF or CNPJ" TEXT CHECK(LENGTH("CPF or CNPJ") <= 30),
                EmpresaName TEXT CHECK(LENGTH(EmpresaName) <= 30),
                Fundacao DATE
            );'''
            cursor.execute(createTableToken)
            connection.commit()
            print("Tabela Criada!")

            standardUser = ('standardUser', 'None')
            standardUserSqlCommand = '''INSERT INTO user_token_activate (username_access, token_activation) VALUES (?, ?)'''
            cursor.execute(standardUserSqlCommand, standardUser)
            connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
            return False
    
    @staticmethod
    def _returnTokenUser() -> str:
        connection = InitDataBase._openConnectDb()
        cursor = connection.cursor()
        token = cursor.execute('''SELECT token_activation FROM user_token_activate WHERE id=?''', (1, )).fetchone()[0]
        connection.close()
        return token
        
    @staticmethod
    def _close(connection: sqlite3.Connection ) -> None:
        '''Fecha conexao com o banco de dados'''
        connection.close()
            
'''Tabelas 
Usuario ADM(tem dois usuarios, o UserInitial e o usuario do sistema) e seus dados;
Tabela Animais;
Tabela Terceiros( São os proprietarios ou criadores que se relacionam com o usuario )'''