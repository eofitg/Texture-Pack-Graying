# Texture-Pack-Graying
A grayscaling tool for Minecraft 1.8.9 texture packs.

------------

### TO-DO
- [ ] Rewrite `operating_tools` - to fix bugs related to paths
- [ ] Complete `clean` - to clean up first before building
- [ ] Complete *isolation system* to enable the separation of block textures and held item textures into different modules.

### Usage
* Put your texture packs in `./input/` folder, can be folders or `.zip` files
* Run `./main.py` anyway 
* Check `./output/` folder

Modify `config.yml` to discover your own unique visual effect.

### Known Bugs
* `operating_tools.py`: `copy_anyway()`
  * Can't work rightly on files / folders like
    * `.Dsine`
    * `1.8.9`

### Credits
* [Merryzz](https://www.youtube.com/@Merryzz) (fr)
* Anyone tolerating my horrible English

------------

**NOTE:**

Sometimes, going check sources yourself may be better than asking for help.