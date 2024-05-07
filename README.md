· Módulo read_extensions.py: Este módulo contém funções específicas para ler diferentes tipos de arquivos, como CSV, JSON, Excel e arquivo de texto. Cada função de leitura lê o arquivo correspondente e chama as funções de processamento de dados do módulo "process_data.py" para realizar a limpeza e preparação dos dados.
    

· Módulo process_data.py: Este módulo contém funções para processar os dados, incluindo verificação e manipulação das colunas, conversão da coluna de data para datetime e índice, remoção de valores nulos e ordenação do DataFrame. Também fornece funções para filtrar o DataFrame por datas ou índices e para deslocar uma coluna por um número específico de períodos.


· Arquivo main.py: Ponto de entrada principal do programa. Ele importa os módulos necessários e define uma função "read_clean" para ler e limpar um arquivo de dados. Além disso, demonstra exemplos de uso das funções de filtragem e deslocamento dos dados após a limpeza.
