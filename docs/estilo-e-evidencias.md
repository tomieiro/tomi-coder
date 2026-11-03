# De onde veio a BASE

Análise realizada em 2026-11-03 sobre os seis repositórios locais de `examples`.
Foram lidos arquivos atuais, históricos de todas as refs disponíveis, estatísticas
de commits selecionados e diffs de sequências de implementação. Nenhum exemplo
foi modificado ou executado.

## Método e limites

O ponto de partida foi `git log --all --no-merges --reverse --author=tomieiro -i`,
comparado ao log geral e aos autores dos commits. Foram considerados os nomes
Matheus Tomieiro, MatheusTomieiro, matheustomieiro e tomieiro encontrados nos
históricos. Merges não foram tratados como autoria da implementação integrada.

Os seis clones informaram não ser shallow. Isso descreve o clone disponível;
não comprova que todas as branches históricas ou trabalhos não publicados estejam
presentes. A análise é qualitativa, não um censo linha a linha nem uma prova de
como o autor pensava. Cada inferência abaixo tem um limite explícito.

Foi dada prioridade a sequências de 2019–2023 para entender a evolução original.
Os ajustes de 2026 em `lesc-evolution` e `std-moon` foram observados como uma fase
posterior; autoria Git não permite determinar se houve auxílio de ferramentas.
Os projetos coletivos contêm contribuições de outras pessoas.

Os caminhos citados são relativos a cada exemplo, no commit indicado quando
diferem da árvore atual. Para conferir uma evidência local:

```sh
git -C examples/InternetRelayChat show 8bbe39f -- src/lista_clientes.h src/lista_clientes.c src/servidor.c
git -C examples/InternetRelayChat show b840161 -- src/servidor.c
git -C examples/std-moon show 388bb9e -- fila.lua
```

## Evidências e decisões

| Projeto e commits | Observação verificável | Consequência para a BASE | Limite |
| --- | --- | --- | --- |
| `std-moon`: `13e150a` → `388bb9e` → `296c189` (2020) | Primeiro surgem arquivos de estruturas vazios; depois uma fila com estado e operações; depois pilha, vetor e documentação. | Pensar em peças nomeadas pelo domínio e preenchê-las em fatias. | Não tornar arquivos vazios uma exigência; criar somente o necessário à fatia atual. |
| `std-moon`: `34ac43d` (2020) | A operação de cópia de lista passa a usar uma função recursiva; também há ajustes em outros arquivos. O diff de `lista.lua` mostra a troca concreta. | Corrigir a operação responsável quando o comportamento exige mudar a representação/cópia. | O commit não demonstra que todos os casos de cópia ficaram corretos. Não copiar a implementação histórica. |
| `std-moon`: `29d1155` (2022), `4ffac4e` (2026) | Estruturas são movidas para `DataStructures`, algoritmos ganham `Algorithms`; depois as pastas passam a nomes minúsculos. | Organização pode amadurecer depois que as responsabilidades já existem. | Renomear pastas não é requisito para todo projeto; a etapa de 2026 não prova o processo manual original. |
| `lesc-evolution`: `2124a5a` → `93d5bab` (2020) | A estrutura separa evolução, GUI e entrada; Makefile compila peças. Constantes e mapa ficam explícitos em `const/macros.h`. | Separar responsabilidades reais e deixar parâmetros importantes visíveis. | Não impor C++, macros, headers separados ou essa árvore a outras linguagens. |
| `lesc-evolution`: `293c12f` (2020) | O diff troca `std::vector` por arrays alocados e atualiza acesso, contagem de passos e liberação no `main`. | Quando uma representação muda, acompanhar seu uso e ciclo de vida. | A mensagem “Trocado para vetor!” não significa adoção de `std::vector`; o diff mostra o contrário. Não inferir melhoria de segurança ou recomendar alocação manual. |
| `lesc-evolution`: `b23f428`, `8f7e2e9`, `b5af886` | Estatísticas mostram rodadas localizadas e, em 2026, ajustes de build e retirada de binários versionados. | O trabalho evolui por revisões; artefatos/build merecem uma etapa explícita. | Estatísticas e títulos não bastam para atestar a qualidade das correções. |
| `InternetRelayChat`: `d4f7115`, `5089c7d` (2020) | O primeiro esboço é pequeno; depois há mudança ampla de C++ para C, com módulos de cliente, servidor e lista. | Não existe uma arquitetura única imutável no histórico; a divisão acompanha o problema. | Uma reescrita histórica não autoriza reescrever projetos atuais. |
| `InternetRelayChat`: `0c17b13` → `89f0dbe` (2020) | Mudanças em listas de canais/clientes são seguidas por integração em servidor e GUI, segundo os arquivos tocados. | Uma capacidade atravessa os módulos que a usam; avaliar o fluxo completo. | A palavra “testados” no commit não prova teste automatizado nem TDD. |
| `InternetRelayChat`: `8bbe39f` → `b840161` (2020) | Mute/unmute acrescentam estado no cliente, busca e chamadas no servidor; depois aparecem guardas para cliente não encontrado. | Construir operações concretas e revisar casos de erro em rodadas. | A BASE exige testar esses casos antes de corrigir; não reproduzir a desreferência insegura inicial. |
| `AdoPet`: `a8862ea` → `cd26f55` (2019) | Controllers de telas nascem como esboços; depois a tela de disponíveis liga dados à exibição e ajusta sua assinatura e consumidores. A árvore distingue `backend`, `bd` e `frontend`. | Criar pontos de integração claros, preencher uma tela/capacidade por vez e atualizar chamadores. | Projeto coletivo; não atribuir toda a arquitetura ou classes de domínio ao usuário. Não transportar estado estático e acoplamentos automaticamente. |
| `AdoPet`: `f2cbb2e`, `581a12b` (2019) | Estatísticas identificam correções concentradas em `BDConexaoClass.java` depois de commits descritos como finalização. | “Finalizado” é um marco provisório; revisar e corrigir continua necessário. | Esses dois commits foram usados como evidência de sequência/escopo, não como prova de correção do banco. |
| `lua_notebook`: `b505925` → `66580be` → `b59813b` → `0c73e6e` (2021) | Começa com `notebook.lua` consumindo `runtime.lua`; a UI cresce, um callback liga entrada à execução, e depois leitura da saída e fechamento do arquivo são ajustados. | Uma separação de dois arquivos pode ser suficiente: coordenação e operação. Integrar o resultado cedo e revisar o ciclo de vida. | O título “callbacks and asserts” acompanha um TODO de assert, não uma suíte comprovada. Execução dinâmica não é modelo seguro para entrada não confiável. |
| `LicensePicker`: `a38c26d` → `7268059` → `ff0ff9e` → `4226206` (2023) | O projeto Android começa concentrando coordenação na Activity e recursos em assets/layouts; depois remove teste de exemplo e muda arquivos ignorados, incluindo o JAR do wrapper. | Aceitar estrutura nativa da plataforma e decomposição por operações sem inventar camadas. | Só há uma sequência curta de implementação. Não copiar source; licença própria atual não está clara. Gradle configurado não significa wrapper completo e executável. |

## Como o ciclo de mudanças aparece

O padrão recorrente é **dar nome às peças → implementar operações → conectar
o comportamento → corrigir casos reais → reorganizar quando necessário**.
Isso não significa que toda alteração seja pequena: o IRC inclui uma troca
ampla de estrutura, e o `std-moon` começa com vários arquivos antecipados.
Também não significa separação arquitetural perfeita: há coordenação e regras
misturadas em pontos dos exemplos.

A interpretação operacional é preservar o raciocínio por domínio, dados e
operações, com liberdade para começar pequeno. A BASE não replica acidentes do
histórico: binários versionados, riscos de memória, estado global compartilhado,
credenciais, dependências incompletas ou nomes inconsistentes.

### O que o histórico não permite concluir

- Que TDD já era uma prática constante. TDD é uma exigência atual do usuário.
- Que todo teste atual foi escrito antes do código ou pelo usuário.
- Que a ordem temporal de commits sempre corresponde à ordem de escrita.
- Que a versão atual representa somente trabalho manual original.
- Que todos os projetos devem ter GUI, classes, Makefile ou as mesmas pastas.
- Que erros são parte obrigatória de uma implementação com aparência humana.

## Transformação para as três skills

`prepare` conserva a organização por peças, mas põe testes e contratos antes
do comportamento. `develop` conserva implementação direta e ligação incremental,
usando a economia do Ponytail para mudanças existentes. `construct` explicita
a rodada posterior de revisão, correção, build e teste do resultado.

O refinamento posterior não adia uma falha concreta já conhecida. Ele permite
adiar polimento e arquitetura especulativa, enquanto os comportamentos de cada
fatia permanecem testáveis e as limitações são declaradas.

## Proveniência e licença

As instruções da BASE são uma síntese original de decisões, não cópia do source
dos exemplos. Os projetos AdoPet, InternetRelayChat, lesc-evolution, lua_notebook
e std-moon apresentam MIT nas licenças locais. A licença raiz de LicensePicker
foi movida para um asset em seu histórico; a presença de textos de licenças em
assets não licencia automaticamente o app. Foi usado apenas para observação.

A adaptação de Ponytail é identificada separadamente e conserva o aviso MIT da
revisão de origem. O projeto tomi-coder mantém sua licença Apache-2.0 existente.
