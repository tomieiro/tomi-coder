---
name: tomi-coder-prepare
description: Preparar projetos e funcionalidades no estilo Tomi, lendo a estrutura existente, escolhendo ferramentas e criando testes antes da implementação. Use para iniciar apps, scripts, módulos ou preparar uma mudança em TDD.
---

# Tomi Coder Prepare

Leia [a BASE](references/BASE.md). Sua entrega é uma fatia preparada com testes
RED e estrutura mínima para desenvolvimento. Sempre TDD.

Ao preparar um objeto ou módulo novo, consulte o
[exemplo de contrato, teste e stub](references/tdd-example.md), adaptado de
código do autor. Ele mostra como chegar ao RED sem implementar a funcionalidade.

## Entender antes de estruturar

Localize a raiz, instruções locais, manifesto AICP se houver, estado do Git,
README, manifests, lockfiles, testes e CI relevantes. Preserve mudanças locais.
Confira a arquitetura no código. Em projeto vazio, derive a primeira fatia do
pedido; em projeto existente, encontre o módulo dono e seus consumidores.

Defina o comportamento observável, o estado envolvido e as fronteiras de entrada
e saída. Pergunte apenas o que realmente bloqueia essa definição; escolha
detalhes reversíveis por evidência e registre a suposição. Não monte uma árvore
genérica antes de compreender a funcionalidade.

## Escolher ferramentas automaticamente

Leia [a seleção de ferramentas](references/builders.md) quando precisar escolher
ou reparar ambiente, runner ou build. Preserve o que já funciona. Diferencie
gerenciador de ambiente, dependências, executor de tarefas e compilador/build.
Verifique executável, versão, manifesto e comandos; presença de um nome no
README não garante que o comando exista. Não invente comandos para `riema` ou
outra ferramenta não identificada.

## Preparar em TDD

1. Se houver testes existentes, rode a menor base relevante e separe falhas
   anteriores da mudança. Não corrija problemas alheios silenciosamente.
2. Escreva primeiro o teste da primeira fatia: sucesso e os erros que fazem
   parte do contrato. Use o runner existente ou o mecanismo mínimo adequado.
3. Prepare só o bootstrap que permite executar esse teste. Depois do teste,
   adicione stubs/assinaturas sem comportamento se necessários. Crie pastas
   quando tiverem função nessa fatia: teste, domínio, entrada, recurso ou saída
   gerada. Não copie a árvore de um exemplo indiscriminadamente.
4. Execute e confirme RED pelo comportamento ausente, seguindo a distinção
   entre falha comportamental e falha de ambiente descrita na BASE.
5. Deixe os comandos de teste/build e as dependências declarados no mecanismo
   escolhido. Gere wrappers/lockfiles com suas ferramentas; não invente hashes
   nem versões. Se o ambiente impedir o RED, entregue a preparação como bloqueada.

Não implemente lógica funcional nesta etapa para fazer o teste passar. Não
precisa escrever todos os testes de um app futuro: prepare uma fatia verificável
e repita o ciclo conforme o escopo avançar. Um teste não deve codificar a solução
interna nem limitar artificialmente o requisito.

## Entrega

Registre a passagem definida na BASE: contrato, responsabilidades, arquivos,
ferramentas e motivo, comandos reais, RED observado e limitações. Se só foi
pedida preparação, encerre declarando os testes intencionalmente vermelhos.
Se o pedido inclui desenvolver/construir, continue para a próxima etapa sem
pedir nova confirmação de rotina.
