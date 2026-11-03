# Escolher o caminho executável mais curto

Esta tabela orienta a escolha; não é um catálogo de comandos prontos para rodar.
Os alvos, versões e opções vêm dos arquivos reais e das ferramentas disponíveis.

| Evidência ou necessidade | Preferência | Verificação antes de usar |
| --- | --- | --- |
| Build/runner existente e CI coerente | Manter a cadeia atual | Ler scripts, receitas, versões e lockfiles; executar a menor verificação relevante. |
| JVM/Android com Gradle | Wrapper do projeto | Conferir scripts, JAR/propriedades e tarefas definidas; distinguir testes locais dos que exigem dispositivo/SDK. |
| Projeto com Maven | Wrapper existente, se disponível | Conferir POM, plugins e fases necessárias; não migrar para Gradle por preferência. |
| C/C++ pequeno | Makefile simples, se não houver ferramenta estabelecida | Conferir compilador, fontes, headers, flags e bibliotecas; separar compilar de executar. |
| CMake, Meson ou outra cadeia já presente | Preservar | Usar configuração e diretório de saída existentes; não empilhar Makefile sem necessidade. |
| Python pequeno | Ambiente virtual e runner já disponível ou biblioteca padrão | Conferir versão, imports, manifesto e forma real de execução; um script pode não precisar de empacotamento. |
| Python com bibliotecas nativas/ambiente Conda declarado | micromamba, quando instalado e compatível | Conferir arquivo de ambiente, canais, plataforma e ambiente alvo; não substituir ferramentas funcionais. |
| JavaScript/TypeScript | Scripts do projeto e gerenciador indicado pelo lockfile | Ler `package.json`, runtime e scripts; conflitos entre lockfiles precisam ser resolvidos por evidência. |
| Rust ou Go | Ferramentas nativas do projeto | Conferir manifests, versão e targets; não acrescentar wrapper apenas por uniformidade. |
| Lua ou shell pequeno | Interpretador e runner simples | Conferir módulos, diretório de execução e código de saída dos testes; não exigir compilação inexistente. |
| Ferramenta citada como `riema` ou nome desconhecido | Investigar antes de escolher | Procurar configuração local, documentação e executável; pedir identificação se indispensável. Não presumir alias ou corrigir o nome silenciosamente. |

## Critérios

1. A ferramenta deve servir ao projeto, ao ambiente e à primeira fatia. Não
   escolher por popularidade nem instalar várias para decidir depois.
2. Use o que o repositório declara. Se estiver quebrado, diagnostique a falha
   antes de migrar. Em projeto novo, prefira suporte nativo e poucas peças.
3. Teste, build e execução são operações distintas. `make` pode abrir uma GUI;
   `build` pode publicar; um script de dependências pode exigir privilégios.
   Leia o conteúdo antes de executar e mantenha ações dentro da autorização.
4. Descreva diretório, ambiente, comando e artefato esperado. Para linguagem
   interpretada, registre que não há compilação e indique teste e smoke test.
5. Se adicionar uma dependência, justifique o que a biblioteca padrão ou o
   conjunto instalado não cobre. Use versões compatíveis verificadas e preserve
   a licença e os mecanismos de resolução existentes.
6. Faça um smoke test do mecanismo antes de interpretar a falha do teste novo.
   Falha de download, SDK, display ou runner não demonstra comportamento ausente.

Não execute instalações globais ou comandos privilegiados por conveniência.
Se a ferramenta necessária não estiver disponível, use uma alternativa local
compatível apenas quando ela preservar o contrato; caso contrário, registre
o bloqueio e continue a preparação independente.
