# Pet Image Classifier

This project uses pretrained CNN models (VGG, AlexNet, ResNet) to classify pet images and determine whether an image shows a dog or not.

## How to run

```
cd data
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

You can also run all three models at once:

```
sh run_models_batch.sh
```

## Project structure

- `data/` - contains the main code, pet images, uploaded images, and model outputs
- `project-workspace-*` - individual workspace folders for each project step
