



# Webhook
  
Crie um Webhook para que o robô possa aguardar uma solicitação antes de prosseguir; a URL será '0.0.0.0:porta/ponto de extremidade.  

*Read this in other languages: [English](Manual_Webhook.md), [Português](Manual_Webhook.pr.md), [Español](Manual_Webhook.es.md)*
  
![banner](imgs/Banner_Webhook.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  







## Descrição do comando

### Criar webhook
  
Com este comando, você pode criar um webhook para que o robô ouça uma solicitação antes de continuar, a url vai ser '0.0.0.0:port/endpoint'
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Endpoint|Endpoint onde você precisa criar uma solicitação, por padrão vai ser '/'|/webhook|
|Porta|Porta onde você precisa criar um webhook, por padrão vai ser '5005'|5005|
|Dados para retornar|Dados que você deseja retornar ao consultar a urlporto/endpoint/uuid route. Este deve ser um objeto que contenha como chave o uuid obtido ao consultar o ponto final e o valor deve ser o que você deseja enviar. Veja o exemplo|{'255de1a0-a6ea-465e-aa6a-0d6b25dd81c6': ['data', 'data2']}|
|Método|Tipo de método para consultar o webhook. Pode ser GET ou POST|GET|
|Variável onde armazenar o resultado|Nome da variável onde armazenar o resultado da consulta. Exemplo 'resultado'||
|Obtenha todos os dados||-|
