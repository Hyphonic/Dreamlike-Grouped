import streamlit as App
import random

# Settings

App.set_page_config(page_title='Dreamlike Grouped', page_icon='⚡', layout='centered', initial_sidebar_state='expanded', menu_items={'Get Help': 'https://huggingface.co/spaces/Hyphonical/Dreamlike-Grouped/discussions/3', 'Report a bug': 'https://huggingface.co/spaces/Hyphonical/Dreamlike-Grouped/discussions/3', 'About': 'https://huggingface.co/spaces/Hyphonical/Dreamlike-Grouped'})
DiffusionMaxBatch = 8 # The maximum batch size for the Diffusion model
DiffusionMaxSteps = 40 # The maximum number of steps for the Diffusion model
PhotoRealMaxBatch = 2 # The maximum batch size for the PhotoReal model
PhotoRealMaxSteps = 20 # The maximum number of steps for the PhotoReal model
MaxQueue = 16 # The maximum number of images that can be queued at once

# Main App

@App.cache_resource(max_entries=1)
def GetUser():
    App.write(App.experimental_user['email'])

GetUser()

App.title('Dreamlike Grouped')
Info = App.expander('Info & Links')

with Info:
    App.markdown('''
    # Dreamlike Grouped
    This is a demo that utilizes the Dreamlike **Diffusion** and **Dreamlike PhotoReal** to create awesome images just for you!
    To get started, simply click on the sidebar and select the model you want to use.
    After that, you give your own input and the model will generate an image based on that, or you can use a random input.
    Then, click on the button below to start the process.
    You can also change the settings to your liking.

    ## Settings
    - **Steps**: The number of steps the model will take to generate the image.
    - **Seed**: The seed of the model. This is the input that the model will use to generate the image.
    - **Prompt**: The prompt of the model. This is the input that the model will use to generate the image.
    - **Batch**: The number of images to generate at once.

    ## FAQ
    ### Why is the model taking so long to generate the image?
    The Model currently used is generating the image using a technique called **Diffusion**. This technique is very slow, but it produces very high quality images.
    ### Why is there a limit of 4 images for the PhotoReal Model?
    The PhotoReal Model is very large, and it takes a lot of memory to generate the images. This is why we have a limit of 4 images at once.
    Dreamlike Diffusion Model is usually faster than the PhotoReal Model.
    ### More Questions?
    If you have any more questions, feel free to create a Discussion, please give as much information as possible.

    ## Links
    - Dreamlike Website: (ttps://dreamlike.art/
    - Official Dreamlike Diffusion Model: https://huggingface.co/dreamlike-art/dreamlike-diffusion-1.0
    - Official Dreamlike PhotoReal Model: https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0
    ''')

# Queue

@App.cache_resource(max_entries=MaxQueue)
def CreateQueue():
    Queue = []
    return Queue

Queue = CreateQueue()

# Sidebar

App.sidebar.title('Dreamlike Grouped')
App.sidebar.subheader('Select Model')
Model = App.sidebar.selectbox('Model', ('Diffusion', 'PhotoReal'))

if Model == 'Diffusion':
    App.sidebar.subheader('Settings')
    Batch = App.sidebar.slider('Batch', min_value=1, max_value=DiffusionMaxBatch, value=1, step=1) # How many images to generate at once
    Steps = App.sidebar.slider('Steps', min_value=1, max_value=DiffusionMaxSteps, value=20, step=1) # How many steps to take to generate the image
    Seed = App.sidebar.text_input('Seed (Leave blank for random)', value='') # The seed of the image
    Prompt = App.sidebar.text_input('Prompt (Leave blank for random)', value='') # The prompt of the image
    Generate = App.sidebar.button(f'Generate {Batch} Image' if Batch == 1 else f'Generate {Batch} Images') # The button to generate the image

    if Generate: # Handles The Queue
        for _ in range(Batch):
            Queue.append({'Model': Model, 'Batch': Batch, 'Steps': Steps, 'Seed': Seed, 'Prompt': Prompt}) if len(Queue) < MaxQueue else Queue.pop(0) and Queue.append({'Model': Model, 'Batch': Batch, 'Steps': Steps, 'Seed': Seed, 'Prompt': Prompt})
        if len(Queue) == 1:
            if Batch == 1:
                App.info(f'Generating Your Image | Capacity ({len(Queue)/MaxQueue * 100})%')
            else:
                App.info(f'Generating Your Images | Capacity ({len(Queue)/MaxQueue * 100})%')

        elif len(Queue) > 1 and len(Queue) <= MaxQueue:
            if len(Queue) == MaxQueue:
                App.warning(f'Queue is full | Capacity ({len(Queue)/MaxQueue * 100})%')
            elif Batch == 1:
                App.info(f'Queued Your Image | Capacity ({len(Queue)/MaxQueue * 100})%')
            else:
                App.info(f'Queued Your Images | Capacity ({len(Queue)/MaxQueue * 100})%')

        else:
            App.error('An unknown error has occurred.')
    
elif Model == 'PhotoReal':
    App.sidebar.subheader('Settings')
    Batch = App.sidebar.slider('Batch', min_value=1, max_value=PhotoRealMaxBatch, value=1, step=1)
    Steps = App.sidebar.slider('Steps', min_value=1, max_value=PhotoRealMaxSteps, value=20, step=1)
    Seed = App.sidebar.text_input('Seed (Leave blank for random)', value='')
    Prompt = App.sidebar.text_input('Prompt (Leave blank for random)', value='')
    Generate = App.sidebar.button(f'Generate {Batch} Image' if Batch == 1 else f'Generate {Batch} Images') # The button to generate the image

    if Generate:
        App.error('The PhotoReal Model is currently not available.')