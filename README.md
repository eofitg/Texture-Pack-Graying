# Texture-Pack-Graying
A grayscaling tool for Minecraft 1.8.9 texture packs.

------------
### TO-DO
- [ ] Make built-in paths configurable
- [ ] Rewrite `operating_tools` - to fix bugs related to paths ✏️
- [ ] Complete `clean` - to clean up first before building ✏️
- [ ] Complete *isolation system* - to enable the separation of block textures and held item textures into different modules

---
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
- The **brightness** parameter does **not work** when a **texture** that needs grayscaling is **absent from the custom pack** (a vanilla texture).

---
### Credits
* [Merryzz](https://www.youtube.com/@Merryzz) (fr) 

------------
### Notes
- Sometimes, it may be more effective to check sources yourself rather than asking for help.