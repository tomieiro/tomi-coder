---
name: tomi-code-construct
description: Construir, testar e revisar implementações segundo a BASE Tomi. Use após desenvolvimento ou para validar mudanças, compilar ou empacotar o projeto, revisar simplicidade e modularidade, detectar falhas e corrigir vulnerabilidades em TDD.
---

# Tomi Code Construct

Leia [a BASE](references/BASE.md). Construa o projeto e confronte implementação,
testes e artefatos com seu contrato. Esta etapa aprofunda correção e segurança
preservando as decisões de domínio, sem reescrever por preferência estética.

Para uma correção localizada, consulte o
[exemplo de revisão antes/depois](references/review-example.md): regressão,
guarda na fronteira correta e preservação do algoritmo. O defeito histórico é
identificado como tal, não como implementação a reproduzir.

## Recuperar e revisar

Leia instruções/contexto arquitetural local, estado do Git e passagem anterior.
Compare o diff com os arquivos completos relevantes, consumidores e testes;
inclua arquivos novos não rastreados. Verifique as evidências de TDD. Se faltarem,
declare a lacuna: testar agora não prova que o desenvolvimento anterior foi TDD.

Confirme se a implementação satisfaz o comportamento pedido e aplique os
critérios de aderência à BASE. Uma função grande ou um arquivo adicional não
constituem defeito isoladamente; procure mistura de responsabilidades, estado
sem dono, duplicação de regra e abstrações sem função concreta.

## Detectar e corrigir falhas

Siga os caminhos alterados e suas fronteiras. Conforme o projeto, examine:

- entradas inválidas, nulos, limites e contratos de erro;
- propriedade de memória/recursos, fechamento, concorrência e cancelamento;
- autorização e isolamento de dados, segredos em código/logs e permissões;
- consultas, shell, caminhos, serialização e execução de conteúdo externo;
- gravações parciais, transações, migrações e recuperação após falha;
- dependências alteradas, compatibilidade e avisos de segurança verificáveis.

Para cada achado real, registre arquivo/local, condição que o dispara, impacto
e evidência. Diferencie confirmado de suspeita. Classifique pelo impacto:
bloqueante (integridade/segurança ou contrato central), relevante (falha concreta
secundária), ou melhoria opcional. Não transforme uma hipótese em vulnerabilidade
confirmada nem diga que um scanner prova ausência de vulnerabilidades.

Corrija os achados dentro do escopo autorizado. Para mudança de comportamento,
crie a regressão, observe RED, corrija e confirme GREEN. Para ajuste estrutural,
garanta caracterização antes e depois. Se a revisão descobrir outra falha,
repita o ciclo necessário. Não afrouxe testes para liberar o build.

Se o pedido for apenas revisão, relate achados e correções propostas sem editar.
Se a correção depender de decisão incompatível com o contrato, ação destrutiva
ou acesso indisponível, registre o bloqueio e continue verificações independentes.

## Construir e verificar o resultado

1. Leia as receitas/scripts antes de executar. Use a cadeia escolhida no
   projeto; reconstitua comandos ausentes por evidência, sem inventar targets.
2. Execute testes afetados e regressões relevantes, análise estática e checks
   exigidos pelo projeto. Use scanners já disponíveis e aplicáveis; registre
   indisponibilidade, cobertura e limitações dos resultados.
3. Gere o artefato local solicitado com o build/empacotamento real. Não modifique
   arquivos gerados manualmente quando houver fonte ou gerador apropriado.
   Separe build de execução, instalação e publicação.
4. Confira o artefato produzido, caminho e formato, e faça um smoke test
   apropriado em ambiente isolado. Scripts sem compilação exigem teste de
   execução ou carga; não invente um build. Se GUI, dispositivo ou serviço
   impedir o smoke, registre que ele ficou sem verificação.
5. Após uma correção, refaça as verificações afetadas e reconstrua artefatos
   invalidados. Revise o diff final e atualize documentação/contexto arquitetural
   quando a mudança alterar seus contratos ou comandos.

Não execute limpeza ampla nem use serviços/dados reais para smoke tests por
conveniência. Não publique, faça deploy, commit ou push sem pedido explícito.

## Entrega

Informe comportamento/artefato produzido, aderência à BASE, correções feitas,
comandos e resultados, achados restantes e limitações. Separe claramente:

- **Concluído no escopo verificado:** checks relevantes passaram, artefato foi
  conferido e não restou achado bloqueante conhecido nesse escopo.
- **Parcial ou bloqueado:** build/teste/smoke necessário não foi executado ou
  falhou, ou resta problema que impede concluir o contrato.

Ausência de evidência não significa aprovação. Compilar com sucesso não prova
correção funcional ou segurança; informe o que foi efetivamente verificado.
