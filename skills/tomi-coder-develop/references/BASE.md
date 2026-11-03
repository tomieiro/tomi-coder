# BASE — desenvolver do jeito Tomi

Esta é a referência comum de `tomi-coder-prepare`, `tomi-coder-develop` e
`tomi-code-construct`. Leia antes de atuar. O estilo foi inferido de arquivos e
diffs dos seis projetos em `examples`; não é uma descrição infalível da pessoa.
O relatório `docs/estilo-e-evidencias.md` do repositório tomi-coder registra as
evidências. As skills instaladas não precisam dos exemplos para funcionar.

## O que vem de onde

- **Pedido atual:** sempre TDD; preparação, implementação e construção/revisão
  em três etapas; BASE para novas funcionalidades; simplificação inspirada no
  Ponytail para alterações; revisão estrutural e de segurança na terceira etapa.
- **Inferência histórica:** pensar em peças concretas, implementar operações
  diretamente, ligar as peças e revisar conforme o comportamento aparece.
- **Limite da inferência:** autoria de commits não prova autoria exclusiva de
  cada linha ou ausência de ferramentas. Projetos coletivos e mudanças de 2026
  não devem ser confundidos com uma assinatura pessoal invariável. O histórico
  consultado não comprova TDD sistemático.

## Como escolher a forma do código

1. **Comece pelo problema visível.** Identifique o que entra, o que muda e o que
   sai. Nomeie as peças pelos conceitos reais: canal, cliente, população, tela,
   execução, relatório. Evite partir de um catálogo de camadas e padrões.
2. **Dê um lugar para cada responsabilidade que já existe.** Um módulo pode
   guardar uma entidade e suas operações; outro coordena a interação com ela.
   Um script pequeno pode ficar em um arquivo. Uma responsabilidade não precisa
   virar serviço, interface e implementação só para parecer modular.
3. **Mantenha os dados compreensíveis.** Campos, parâmetros, coleções e mudanças
   de estado devem ser rastreáveis. Explique quem possui e altera cada recurso.
   Não transforme isso em obrigação de usar estado global, ponteiros ou classes.
4. **Escreva operações concretas.** Funções e métodos expressam ações do domínio.
   Um fluxo curto, com sequência e condições explícitas, é preferível a mecanismos
   genéricos que escondam o trabalho. Use os recursos idiomáticos da linguagem.
5. **Conecte uma fatia utilizável.** Percorra entrada → operação → saída. A GUI,
   CLI, rota ou `main` coordena o fluxo; extraia a regra que precisa ser testada
   sem depender de uma janela, rede ou banco real. Uma extração pequena basta.
6. **Evolua pela próxima necessidade observável.** Faça uma fatia, execute,
   corrija e então avance. Pode haver trabalho intermediário incompleto, desde
   que o estado esteja declarado e o comportamento entregue seja verificável.
7. **Mude a representação quando a atual atrapalhar.** Uma coleção, assinatura
   ou divisão de arquivos pode mudar por uma razão concreta. Proteja o contrato
   com testes e ajuste os consumidores no mesmo trabalho. Não reestruture todo
   o repositório para encaixar uma funcionalidade pequena.
8. **Separe parâmetros de decisão de infraestrutura inventada.** Use constantes
   nomeadas ou a configuração já existente para valores que precisam ser
   entendidos ou ajustados. Não crie um sistema de configuração especulativo.
9. **Escreva para quem continuará o projeto.** Preserve idioma e convenções
   locais. Use nomes do domínio e comentários sobre intenção, limites e contratos.
   Não simule o estilo com erros de digitação, gírias obrigatórias, comentários
   redundantes ou mensagens de commit vagas.

Isso permite uma primeira implementação simples, às vezes ainda pouco polida.
Não exige arquitetura perfeita antecipadamente nem autoriza produzir defeitos
intencionais. Falhas encontradas viram novos testes e correções; limitações
conhecidas ficam explícitas. Validação de entradas externas, proteção de dados
e controles de acesso necessários já fazem parte da primeira fatia.

## Nova funcionalidade e alteração existente

| Situação | Decisão |
| --- | --- |
| Novo app ou capacidade | Defina primeiro comportamento e teste; desenhe as peças concretas da fatia e implemente seguindo esta BASE. |
| Novo arquivo para capacidade existente | Escolha o dono pelo domínio e pela estrutura local; arquivo novo não implica arquitetura nova. |
| Correção ou extensão localizada | Trace chamadores e efeitos; preserve a forma do projeto e aplique a menor alteração completa. |
| Refatoração | Garanta testes de caracterização verdes antes; preserve o comportamento e justifique a mudança de estrutura. |
| Novo projeto minúsculo | Use apenas arquivos e ferramentas necessários ao primeiro comportamento verificável. |
| Projeto com arquitetura estabelecida | Integre as decisões desta BASE às fronteiras existentes; não imponha pastas históricas de outro projeto. |

A BASE orienta a forma de nascer e crescer. A adaptação do Ponytail orienta a
economia da mudança, sem suprimir uma funcionalidade solicitada, uma fronteira
útil ou um teste obrigatório. O objetivo é o menor conjunto **completo** de
mudanças, não a menor contagem de caracteres ou arquivos a qualquer custo.

## Sempre TDD

Para todo comportamento novo, alterado ou corrigido:

1. **Contrato:** descreva uma entrada ou situação, a ação e o resultado esperado.
   Use a interface observável e critérios do pedido, não detalhes inventados da
   implementação. Inclua casos de erro que pertençam ao contrato da fatia.
2. **RED:** escreva o teste antes da implementação e execute-o. Confirme a falha
   esperada e seu motivo. Comportamento ausente é RED; erro de ambiente,
   dependência indisponível ou teste que não foi descoberto não comprova RED.
3. **GREEN:** implemente só o necessário para cumprir o contrato. Execute o mesmo
   teste e a regressão afetada. Um caso artificialmente codificado para satisfazer
   uma única amostra não implementa o contrato.
4. **REFACTOR:** melhore apenas o que já tem justificativa, com os testes verdes.
   Preserve as fronteiras do domínio e a legibilidade da sequência de operações.

Não implemente a funcionalidade para depois escrever o teste. Não enfraqueça
asserções, marque testes como ignorados ou mude o resultado esperado apenas
para obter GREEN. Se o requisito mudou, registre a mudança do contrato.

**Bootstrap:** é permitido criar primeiro o mínimo necessário para rodar testes
(manifesto de dependências, runner, diretório, assinatura/stub sem lógica). Crie
o arquivo de teste antes do source funcional. Se um import ausente impede a
asserção, use o stub mínimo para chegar à falha comportamental. Não implemente
regra de negócio nessa preparação. Evite levantar um app inteiro para testar
uma regra que cabe em uma função.

**Legado:** caracterize primeiro o comportamento que precisa permanecer. Para
o defeito, acrescente uma regressão que falha antes da correção. Para refatoração
sem mudança de comportamento, testes de caracterização podem começar verdes;
não invente um defeito só para obter RED.

**Estrutura, build e configuração:** quando alterarem comportamento executável,
use um teste de contrato, integração ou smoke test antes da mudança. Para uma
mudança puramente documental, valide referências e consistência; não fabrique
um teste que apenas compara a redação do texto.

**Ambiente bloqueado:** registre comando, impedimento e o que falta. Pode
continuar inspeção, testes e preparação independente; não declare RED/GREEN nem
avance para implementar o comportamento dependente sem poder observar o ciclo.

## Passagem entre etapas

Use o registro de tarefa existente. Se não houver e for necessário retomar em
outra sessão, crie um único `TOMI-TASK.md` na raiz; não sobrescreva outras tarefas.
No fluxo contínuo curto, o registro pode ser a mensagem de passagem. Leve adiante:

```text
Objetivo e contrato observável:
Fatia atual e responsabilidades dos módulos:
Arquivos de teste e implementação envolvidos:
Ferramentas escolhidas e evidências da escolha:
Comandos (diretório, ambiente, teste, regressão, build, smoke):
RED: comando, teste, falha observada, estado do código:
GREEN: comando, resultado, estado do código, ou ainda não executado:
Limites deliberados, riscos e bloqueios:
Próxima etapa e pendências:
```

Comandos são concretos e verificados no projeto; campos inaplicáveis recebem
uma justificativa curta. Registre resultados reais, não resultados pretendidos.
Use commit se já existir ou uma descrição dos arquivos/diff; não crie commits
automaticamente. Mudanças posteriores invalidam a evidência afetada.

- **prepare → develop:** estrutura mínima e testes RED comprovados, comandos e
  contratos definidos. RED é uma entrega esperada de preparação, não app pronto.
- **develop → construct:** fatia implementada e testes afetados GREEN; indicar
  limites e revisões pendentes. Não prometer que o projeto está seguro ou pronto
  para distribuição antes da verificação.
- **construct → conclusão:** revisão contra a BASE, regressão, build ou equivalente
  e smoke test do artefato; apontar exatamente o que passou, falhou ou foi bloqueado.

Se uma etapa for invocada sozinha, reconstitua os pré-requisitos e execute o que
estiver faltando dentro do escopo autorizado. Não exija que o usuário invoque
outra skill apenas para cumprir uma dependência. Em um pedido pelo ciclo inteiro,
avance automaticamente entre as etapas, preservando seus critérios de saída.

## Limites operacionais

Leia instruções locais e contexto arquitetural antes de editar; confronte-os com
os arquivos reais. Preserve alterações do usuário. A BASE não autoriza publicar,
executar migrações destrutivas, instalar ferramentas globalmente ou alterar
serviços externos. Build local não implica deploy. Não execute targets de nome
inofensivo sem ler sua receita: podem abrir serviços ou instalar pacotes.

Segurança e integridade não são acabamento. A terceira etapa aprofunda a revisão,
mas um problema concreto encontrado antes deve ser testado e corrigido na etapa
atual. Melhoria estética e generalização futura podem esperar; perda de dados,
exposição de segredos e quebra conhecida de contrato não devem ser disfarçadas
como parte do estilo.

## Critério de aderência à BASE

Na revisão, procure evidências, sem nota numérica artificial:

- Cada módulo corresponde a uma responsabilidade real e pode ser compreendido
  a partir de seus dados, operações e consumidores?
- O caminho entre entrada, mudança de estado e saída está claro?
- A mudança respeita os contratos existentes e alcança todos os consumidores?
- Há teste anterior para o comportamento e evidência do ciclo executado?
- A solução usa a estrutura existente e só adiciona abstrações justificadas?
- As limitações estão explícitas e o próximo ajuste pode ser localizado?

Uma divergência pede correção quando prejudica o comportamento, a modularidade,
a segurança ou a manutenção concreta. Diferença de gosto não justifica reescrita.
