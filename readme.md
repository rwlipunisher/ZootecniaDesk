Software Desenvolvido por EstrategistA
Documentação simplificada do projeto: 
Esquema de diretorios: 

DiretorioRaiz da Aplicação/
├── VirtualEnv #Virtual Enviroment da aplicação 
│
├── main.py                  # Index da aplicação
│
├── models/
│   ├── __init__.py
│   ├── database_model.py   # Database Model (SQLite operations)
│   ├── activation_token_model.py  # Model de Ativação por Tokens
│   └── general_parameters_model.py # Model de paramentros Gerais da Aplicação
│
├── views/
│   ├── __init__.py         
│   ├── main_window_view.py # Janela principal da Aplicação
│   ├── activation_token_view.py  # Janela de ativação pro token da aplicação
│   └── general_parameters_view.py # Janale de configuração de paramentros gerais da aplicação
│
├── controllers/
│   ├── __init__.py         # Initialize the controllers package
│   ├── main_controller.py  # Controlador principal
│   ├── activation_token_controller.py  # Controlador de Ativação por Token
│   └── general_parameters_controller.py # Controlador de configuraçãod e paramentros gerais da aplicação
│
├── resources/
│   ├── images/             # Imagens utilizadas na aplicação
│   ├── icons/              # icones utilizadas na aplicação
│   └── ...
│
├── data/
│   ├── myapp.db            # SQLite3 DB
│   └── ...
│
└── README.md               # Documentação do Projeto.
