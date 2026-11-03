# tomi-coder

Três skills para desenvolver no estilo Tomi: peças concretas do domínio,
implementação direta, integração incremental e revisão posterior. **Sempre
TDD: teste antes do comportamento, RED observado, GREEN e refatoração.**

A [BASE](BASE.md) foi construída a partir da leitura dos seis projetos locais
em `examples` e de seus históricos. O [relatório de evidências](docs/estilo-e-evidencias.md)
relaciona commits, observações e limites da interpretação. O histórico não prova
TDD sistemático: essa é uma exigência atual incorporada às skills.

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
execução por agentes em todos esses ambientes. Os exemplos foram apenas lidos.
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

A BASE e as demais instruções foram redigidas originalmente a partir de
observações dos projetos, sem copiar seu source. `examples/` mantém as licenças
e autorias próprias; sua presença local não muda a licença desses projetos.
