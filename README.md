# kindle2anki
Convert Kindle Vocabulary to Anki Deck

1.- Conectar el Kindle por USB y obtener el fichero vocab.db de Kindle/system/vocabulary/vocab.db
2.- Ir a fluentcard.com para generar los los deck por libro y exportarlos a TSV
3.- Correr el script kindle2anki para añadir significado y preparar el fichero deck.tsv para importar en Ankiapp
4.- Ir a https://api.ankiapp.com/nexus/ para importar el deck a tu cuenta Ankiapp
5.- Descargar el deck en Ankiapp y prepararle un layout con data-type='tts' en el campo del front para que lo lea