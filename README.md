# Atualizações do xciptv Android

Canal público de APKs de distribuição assinados. O código-fonte e a chave Android ficam no repositório privado `alexmetaloide/xciptv`.

Baixe o APK em **Releases**. As compilações debug do repositório de código são exclusivas para testes e não atualizam a versão de distribuição.

O app consulta este canal e usa o instalador do Android para confirmar a atualização, preservando dados quando o APK tem o mesmo pacote e certificado. As betas antigas com outra assinatura precisam de uma migração única após salvar os dados necessários.

Quando o workflow privado enviar `apks/` e `release.json`, o workflow público verifica o checksum e cria a Release correspondente. Os secrets de assinatura nunca são enviados a este repositório.
Canal público de APKs assinados do xciptv. O código-fonte permanece privado.
