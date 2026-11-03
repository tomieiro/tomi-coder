# Ponytail adaptado ao fluxo Tomi

Derivação de [Ponytail, por DietrichGebert](https://github.com/DietrichGebert/ponytail),
arquivo `skills/ponytail/SKILL.md`, revisão
`96608e078b2d5ea607c5c3b8b5a54d1c1fba6846`.
Copyright (c) 2026 DietrichGebert. Origem sob MIT; o aviso original acompanha
esta adaptação em [PONYTAIL-LICENSE](PONYTAIL-LICENSE).

Esta adaptação se aplica ao trabalho desta skill, sem ativação persistente em
outras tarefas. Não exige instalar o Ponytail original. BASE, TDD obrigatório e
o pedido do usuário delimitam a simplificação.

## Antes de reduzir a solução

Entenda o fluxo real, os chamadores, os contratos e os efeitos da mudança.
Economizar leitura pode produzir uma alteração pequena no lugar errado.

Escolha a primeira solução que cubra completamente a necessidade:

1. Remova do plano somente o que foi imaginado para um futuro não solicitado.
2. Reuse uma operação, componente ou convenção já existente no projeto.
3. Use biblioteca padrão ou recurso nativo compatível com a estrutura local.
4. Reuse uma dependência instalada que resolva o problema.
5. Escreva a menor implementação legível que cumpra o contrato restante.

Não acrescente interfaces sem necessidade, wrappers vazios, configurações sem
uso nem camadas cujo único propósito seja parecer arquitetura. Preserve as
fronteiras úteis existentes. Poucos arquivos não justificam misturar UI,
persistência e regras num módulo impossível de testar.

Para bugs, corrija a causa no ponto compartilhado quando ele for o responsável.
Verifique os consumidores e ajuste o que a mudança afetar. Código movido mantém
tratamento de erros e validação. Uma linha críptica não é uma simplificação.

Anote um limite deliberado somente quando ele for relevante: qual é o limite e
qual condição concreta exigiria mudá-lo. Não invente cenários para justificar
infraestrutura antecipada.

## Diferenças deliberadas em relação à origem

- TDD é obrigatório mesmo em comportamento pequeno; não herdamos a dispensa
  de testes para mudanças triviais do Ponytail.
- A decomposição de novas funcionalidades vem da BASE, não de minimizar o
  número de arquivos isoladamente.
- Não há modo que elimine um requisito explícito em nome de YAGNI.
- O fluxo não impõe respostas telegráficas; relate a evidência e as limitações
  necessárias para revisar o trabalho.

Nunca remova proteção de dados, controles de acesso, validação nas fronteiras,
tratamento de falhas ou requisitos explícitos para encurtar o diff.
