# tomi-coder

Três skills para desenvolver no estilo Tomi: peças concretas do domínio,
implementação direta, integração incremental e revisão posterior. **Sempre
TDD: teste antes do comportamento, RED observado, GREEN e refatoração.**

A [BASE](BASE.md) foi construída a partir da leitura dos seis projetos originalmente
fornecidos em `examples` e de seus históricos. O [relatório de evidências](docs/estilo-e-evidencias.md)
relaciona commits, observações e limites da interpretação. O histórico não prova
TDD sistemático: essa é uma exigência atual incorporada às skills.

Os clones foram removidos por solicitação do usuário após a extração. As skills
preservam [exemplos anonimizados](skills/tomi-coder-develop/references/code-examples.md)
de estado, operações, reuso, lógica, callbacks e navegação, além de um
[exemplo de preparação em TDD](skills/tomi-coder-prepare/references/tdd-example.md)
e uma [revisão antes/depois](skills/tomi-code-construct/references/review-example.md).
O [registro de proveniência](docs/code-provenance.md) identifica arquivos, commits,
autoria por linha e alterações deliberadas. Os nomes do domínio são neutros;
os avisos de autoria e licença continuam preservados.

## As três etapas

| Skill | Responsabilidade | Entrega |
| --- | --- | --- |
| [tomi-coder-prepare](skills/tomi-coder-prepare/SKILL.md) | Ler o existente, escolher ambiente/build/runner, definir a estrutura mínima e escrever os testes primeiro. | Contrato, comandos, stubs necessários e RED confirmado. |
| [tomi-coder-develop](skills/tomi-coder-develop/SKILL.md) | Implementar novas capacidades pela BASE e alterar código com a economia do Ponytail. | Fatias funcionais, GREEN e regressões afetadas verificadas. |
| [tomi-code-construct](skills/tomi-code-construct/SKILL.md) | Revisar simplicidade, modularidade, aderência à BASE, falhas e segurança; corrigir em TDD e construir. | Resultado local conferido, verificações e limitações explícitas. |

O terceiro nome é **`tomi-code-construct`**, conforme solicitado, sem o `r`
de `coder`. BASE é uma referência comum, não uma quarta skill.

“Humano” significa permitir evolução e refinamento, sem antecipar arquitetura
perfeita. Não significa fabricar bugs ou adiar uma vulnerabilidade já conhecida.
A revisão da terceira etapa aprofunda os cuidados presentes desde a primeira.

## Usar

Exemplos de pedidos após instalar as skills:

```text
Use $tomi-coder-prepare para preparar um script que agrupa despesas de um CSV.
Use $tomi-coder-develop para implementar a fatia preparada e deixar os testes verdes.
Use $tomi-code-construct para revisar, corrigir e construir o resultado.
```

Para o ciclo inteiro, peça as três etapas no mesmo trabalho. Elas devem continuar
sem confirmação de rotina entre fases. Quando só a preparação for solicitada,
os testes vermelhos são o resultado esperado. Quando uma etapa for chamada sem
passagem anterior, ela reconstitui os pré-requisitos necessários.

Cada pasta em `skills/` é autocontida: leva sua cópia da BASE e suas referências.
Pode ser instalada individualmente; não precisa dos repositórios de exemplo.
Copie a pasta completa da skill desejada para o diretório de skills do seu
agente. Para Codex, use `$CODEX_HOME/skills` quando definido, ou
`~/.codex/skills`. Preserve uma instalação existente antes de substituí-la.
Este repositório entrega os arquivos; não altera automaticamente sua instalação.

As ferramentas de projeto são selecionadas por evidência: preservar a cadeia
existente, preferir recursos nativos, conferir comandos e separar ambiente,
dependências, testes, build e execução. Makefile, Gradle ou micromamba são opções
condicionais. Um nome não identificado, como `riema`, precisa ser investigado;
a skill não inventa seus comandos.

## Manter e verificar

Edite **somente a BASE canônica na raiz** e sincronize suas cópias antes de
distribuir. As cópias em `references/BASE.md` são artefatos gerados por cópia exata.
Python 3 é suficiente; GNU Make é opcional:

```sh
python3 scripts/sync_base.py --write
python3 -m unittest discover -s tests -v
python3 scripts/sync_base.py
```

Ou use `make sync-base` e `make check`. Sem `--write`, o sincronizador apenas
verifica e retorna código 1 se encontrar cópia ausente ou diferente. Os testes
usam diretórios temporários e verificam cópia exata, detecção sem escrita,
ausência da fonte e os códigos de saída da CLI.

A suíte também extrai os trechos diretamente do Markdown e verifica seu
comportamento com Lua, GCC, G++ e JDK (`javac`/`java`). São oito verificações de
exemplos, incluindo RED → GREEN do exemplo de preparação, além dos quatro
testes do sincronizador. Ferramentas ausentes geram testes explicitamente
ignorados; uma validação completa exige as ferramentas e nenhum teste ignorado.
Os builds e execuções usam diretórios temporários e dispensam os clones originais.

Se a skill `skill-creator` estiver disponível, execute também seu
`scripts/quick_validate.py` para cada uma das três pastas. Esse validador confere
o formato de skill, não a qualidade de decisões futuras do agente.

Para revisar mudanças nas instruções, percorra estes cenários:

| Cenário | Comportamento esperado |
| --- | --- |
| App vazio | Teste antes do source funcional; bootstrap mínimo; RED antes de desenvolver. |
| Bug em legado sem testes | Caracterizar o que permanece e reproduzir o defeito antes de corrigir. |
| Runner/SDK indisponível | Registrar bloqueio; não usar falha de ambiente como RED nem inventar GREEN. |
| Refatoração sem mudança funcional | Caracterização pode começar verde; preservar comportamento. |
| Script sem compilação | Testes e smoke de execução; não inventar build. |
| Achado no construct | Regressão primeiro, correção, novo build se o artefato foi invalidado. |
| Solicitação só de revisão | Achados e propostas, sem editar arquivos. |
| Novo módulo versus mudança local | BASE na decomposição; economia do Ponytail na alteração, preservando TDD. |

Esses cenários são critérios de revisão das instruções, não uma alegação de
execução por agentes em todos esses ambientes. Os projetos originais foram
apenas lidos; seus trechos adaptados possuem testes executáveis.
Não há deploy, commit, push ou instalação global implícitos no fluxo.

## Derivação e licenças

O repositório mantém sua [licença Apache-2.0](LICENSE).

`tomi-coder-develop` inclui uma **derivação adaptada do
[Ponytail](https://github.com/DietrichGebert/ponytail)**, por DietrichGebert,
originalmente sob MIT. A adaptação está em
[references/ponytail.md](skills/tomi-coder-develop/references/ponytail.md), baseada
em `skills/ponytail/SKILL.md` da revisão
`96608e078b2d5ea607c5c3b8b5a54d1c1fba6846`.

O aviso **Copyright (c) 2026 DietrichGebert** e os termos MIT originais estão
preservados em [PONYTAIL-LICENSE](skills/tomi-coder-develop/references/PONYTAIL-LICENSE).
Esse aviso acompanha a adaptação ao distribuir a skill. A adaptação exige TDD
também para comportamentos pequenos e preserva a decomposição da BASE; não
herda modos que possam cortar requisitos explícitos. Não é preciso instalar
o Ponytail original nem baixar seu repositório para usar estas skills.

A BASE foi redigida originalmente a partir de observações dos projetos. As novas
referências de código são derivações MIT de trechos selecionados, com atribuição
e mudanças documentadas. Cada skill leva seu `references/EXAMPLES-LICENSE`:
[prepare](skills/tomi-coder-prepare/references/EXAMPLES-LICENSE),
[develop](skills/tomi-coder-develop/references/EXAMPLES-LICENSE) e
[construct](skills/tomi-code-construct/references/EXAMPLES-LICENSE).
Preserve esses avisos ao redistribuir os trechos. A licença Apache-2.0 do restante
do projeto não substitui os avisos MIT. Nenhum source de LicensePicker foi
reutilizado, pois a licença do app não foi estabelecida.
