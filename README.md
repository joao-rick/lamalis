# LAMALIS

Projeto para comunicação de API's, com foco em mensageria e dockerização.

## Fluxo

API geradora disponibiliza na rota as informações de uma criptomoeda fictícia por vez, contendo:
Nome, sigla, Valor inicial, Valor atual, Nível de risco. Realiza o publish para o exchange do RabbitMQ que encaminha para a fila. Esta, por sua vez, entrega para a segunda APi, a verificadora, categoriza qual tipo de criptomoeda é, com base em informações dinâmicas, contidas no seu banco de dados. Ao realizar a verificação, envia para a "produção", que seria o banco de dados final para armazenamento com as categorias.

## Diagramas

<img width="813" height="881" alt="lamalis drawio (2)" src="https://github.com/user-attachments/assets/8875d73c-b334-40be-b283-9327fb63ad47" />
