# Texture-Pack-Graying
A grayscaling tool for Minecraft 1.8.9 texture packs.

------------

### TO-DO
- [ ] Rewrite `operating_tools` - to fix bugs related to paths ✏️
- [ ] Complete `clean` - to clean up first before building ✏️
- [ ] Complete *isolation system* - to enable the separation of block textures and held item textures into different modules

### Features
- Custom brightness
- Keep cover image `pack.png`
- Blocks
  - Isolating wools and carpets
- OptiFine
  - Animation
  - Block CTM
  - Custom Sky
- Whitelist to keep certain objects

### Usage
* Put your texture packs in `./input/` folder, can be folders or `.zip` files
* Run `./main.py` 
* Check `./output/` folder after seeing
  ```
  ...
  Done.
  ```
Modify `config.yml` to discover your own unique visual effect.

### Known Bugs

### Credits
* [Merryzz](https://www.youtube.com/@Merryzz) (fr)

------------

**NOTE:**

Sometimes, going check sources yourself may be better than asking for help.