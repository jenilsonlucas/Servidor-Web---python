## SERVIDOR WEB

Desenvolvi um servidor web customizado em Python, com o objetivo de aprofundar o entendimento sobre o funcionamento interno de servidores HTTP. O projeto cobre desde o parsing de requisições HTTP até a entrega de respostas, explorando os principais conceitos que sustentam a comunicação cliente-servidor.

Atualmente, o servidor oferece suporte ao método GET, com as seguintes funcionalidades:

- Servir arquivos estáticos diretamente do sistema de arquivos.

- Execução de arquivos dinâmicos, simulando a lógica de servidores que processam conteúdos gerados em tempo real.

- Listagem automática de diretórios, permitindo navegação estruturada quando não há um arquivo index.

## PROXIMOS PLANOS PLANEJADOS:

1. Implementação de outros métodos HTTP (POST, PUT, DELETE, etc.).

2. Exploração de diferentes modelos de concorrência para lidar com múltiplas requisições:

- Threads (paralelismo em nível de sistema operacional).

- Processos (isolamento e maior resiliência).

- I/O assíncrono (maior eficiência em cenários de alto tráfego).

3. Análise de desempenho para comparar os modelos e entender trade-offs de escalabilidade e consumo de recursos.

Este projeto reflete não apenas habilidades práticas em Python e redes, mas também uma abordagem de engenharia exploratória, focada em compreender como servidores web são projetados e otimizados para atender diferentes cenários de carga.
