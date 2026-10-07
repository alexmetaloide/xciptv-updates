# Atualizações do MTPLAYER

Canal público oficial de APKs assinados do **MTPLAYER** para Android e Android TV.

Baixe a versão atual em **Releases**. O mesmo APK atende smartphones, tablets e Android TV/TV Box compatíveis.

O MTPLAYER instalado consulta automaticamente este repositório após iniciar e também pelo botão **Atualizar aplicativo**. Quando existe uma versão mais nova, o app baixa o APK oficial, valida pacote, versionCode, versão mínima do Android e assinatura digital, e então abre o instalador do Android para concluir a atualização preservando os dados.

As versões de distribuição usam o pacote `com.metalloide.iptv` e devem continuar assinadas com a mesma chave permanente. Builds debug são apenas para testes e não participam do canal de atualização.

O pipeline de release envia o APK assinado para `apks/`, atualiza `release.json`, verifica o SHA-256 e cria a Release `android-v<versão>`. A chave de assinatura permanece protegida no repositório de código e nunca é publicada aqui.
