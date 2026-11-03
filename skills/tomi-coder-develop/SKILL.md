---
name: tomi-coder-develop
description: Implementar e alterar código no estilo Tomi usando a estrutura preparada e o ciclo TDD. Use para criar funcionalidades, editar sources e scripts, corrigir bugs ou refatorar, combinando a BASE com mudanças mínimas inspiradas no Ponytail.
---

# Tomi Coder Develop

Leia [a BASE](references/BASE.md). Para alterações em código existente, leia
também [a adaptação do Ponytail](references/ponytail.md). Novas capacidades seguem
a decomposição da BASE; mudanças locais seguem a menor alteração completa.

## Recuperar a fatia

Leia instruções/contexto arquitetural local, alterações pendentes e a passagem
do prepare, quando existir. Abra os testes, os arquivos que serão alterados e
os consumidores relevantes. Trace entrada, dados, operação e saída antes de
decidir onde editar. Verifique o estado real em vez de confiar no relato anterior.

Sem preparação, faça a preparação mínima da BASE: contrato, ferramentas,
teste anterior e RED comprovado. Não espere que o usuário invoque outra skill.
Um teste já verde não comprova RED: descubra se a capacidade já existe, se o
teste não discrimina a mudança ou se o estado avançou desde a passagem.

## Programar

1. Escolha uma fatia verificável. Para novo comportamento, escreva/complete e
   execute o teste antes do source funcional. Para bug, reproduza a falha; para
   refatoração, caracterize o comportamento que deve permanecer.
2. Implemente na estrutura BASE preparada. Dados e operações ficam junto de
   suas responsabilidades; entrada e coordenação conectam as peças. Abra um
   arquivo novo quando houver uma responsabilidade concreta que o justifique.
3. Para edição existente, encontre a causa e seus chamadores. Reuse soluções
   locais, biblioteca padrão e dependências existentes antes de adicionar algo.
   Uma assinatura alterada exige atualizar consumidores, fixtures e exports
   afetados; uma correção em um único chamador pode deixar a causa intacta.
4. Execute o teste da fatia até GREEN e a regressão afetada. Investigue falhas
   sem apagar asserções. Ajuste o contrato apenas quando o pedido justificar.
5. Refatore o que facilita a próxima mudança real, mantendo os testes verdes.
   Não reescreva arquivos adjacentes para uniformizar estética. Repita o ciclo
   para as próximas fatias do escopo autorizado até concluir a implementação.

Código inicial pode ser direto e pouco polido. Não adicione bugs, duplicação
deliberada ou nomes ruins para parecer humano. Não deixe uma quebra conhecida
de contrato ou vulnerabilidade concreta para o construct consertar. Registre
limitações aceitáveis e pontos que merecem revisão mais profunda.

## Entrega

Informe comportamento implementado, arquivos/responsabilidades afetados,
evidência RED → GREEN, regressões executadas e limites. Atualize o registro de
passagem da BASE, sem inventar resultados. Se houver bloqueio, identifique o
que está incompleto; código escrito não equivale a comportamento validado.

Quando o pedido abrange o ciclo completo, avance para construção e revisão.
Não publique, faça commit ou faça push como efeito implícito de programar.
