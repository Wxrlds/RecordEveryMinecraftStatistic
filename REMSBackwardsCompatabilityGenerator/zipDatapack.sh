mkdir data/remsbc/functions/ -p
mkdir data/minecraft/tags/functions/ -p
cp output/setup.mcfunction data/remsbc/functions/
cp ../pack.png pack.png
cp ../readme.md readme.md
echo '{"values":["remsbc:setup"]}' > data/minecraft/tags/functions/load.json
echo 'datapack disable "file/remsbc.zip"' | tee -a data/remsbc/functions/setup.mcfunction
echo 'say remove the REMSBC.zip datapack now and perform a /reload' | tee -a data/remsbc/functions/setup.mcfunction
zip -r REMSBC.zip pack.png pack.mcmeta data/ readme.md
rm -rf data/
rm -rf pack.png
rm -rf readme.md