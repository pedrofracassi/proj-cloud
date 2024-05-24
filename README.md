# Projeto Cloud

Para criar ou atualizar a stack:

```bash
aws cloudformation deploy --stack-name=Cloud --template-file=cloud.yaml
```

Para deletar a stack:

```bash
aws cloudformation delete-stack --stack-name=Cloud
```

## Checklist

### C+

#### EC2 com Auto Scaling:
- [x] Criar um Launch Configuration com uma AMI que tenha a aplicação pré-instalada.
- [x] Provisionar um Auto Scaling Group (ASG) utilizando o Launch Configuration criado.
- [x] Definir políticas de escalabilidade baseadas em CloudWatch Alarms (ex: CPU Utilization > 70%).
- [x] Garantir a integração do ASG com o ALB através do Target Group.

#### Application Load Balancer (ALB):
- [x] Provisionar um ALB para distribuir o tráfego entre as instâncias EC2.
- [x] Configurar Target Groups para gerenciar as instâncias EC2.
- [x] Implementar Health Checks para garantir que o tráfego seja direcionado apenas para instâncias saudáveis.

#### Banco de Dados DynamoDb:
- [x] Provisionar uma instância DynamoDb.
- [x] Configurar Security Groups para garantir que apenas as instâncias EC2 possam se conectar ao banco de dados.

#### Cálculo de Custo

- [x] Utilizar a Calculadora de Custo da AWS para estimar os custos mensais da arquitetura proposta.

#### Documentação

- [x] Criar uma documentação técnica que inclua um diagrama da arquitetura AWS.
- [x] Documentar todas as decisões técnicas tomadas e justificá-las.
- [x] Incluir um guia passo a passo de como executar os scripts que você criou (não esquqeca de validar a sua infraestrutura).
- [x] Elaborar um relatório detalhado com a previsão de custos, destacando os principais gastos e possíveis otimizações.
- [x] Colocar o link do repositorio com o código CloudFormation no Documento.