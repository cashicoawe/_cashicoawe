# where is opengl

- zenn
    - https://zenn.dev/hidenori3/articles/c2be2bd50fc8dd
- linux gpu driver developer's guide
    - https://dri.freedesktop.org/docs/drm/gpu/index.html
- vulkan specification
    - https://registry.khronos.org/vulkan/
    - khronos なんだ...
- nvidia open-gpu-doc
    - https://github.com/NVIDIA/open-gpu-doc
- amd
    - https://wiki.osdev.org/Accelerated_Graphic_Cards#VMware_SVGA-II
    - https://www.amd.com/en/developer.html#open_gpu

```sh
# https://github.com/GPUOpen-Drivers/AMDVLK
# Get Repo Tools  

mkdir ~/  
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo

# Get Source Code

mkdir vulkandriver
cd vulkandriver
~/bin/repo init -u https://github.com/GPUOpen-Drivers/AMDVLK.git -b master
~/bin/repo sync
```
- linux amd
    - https://github.com/torvalds/linux/tree/master/drivers/gpu/drm/amd/amdgpu
- https://www.youtube.com/watch?v=B8xHWwCuxKA
