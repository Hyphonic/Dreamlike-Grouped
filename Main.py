import os, sys, random, string, time, logging
from threading import Thread
from pathlib import Path
from queue import Queue
import gradio as App

logging.basicConfig(level=logging.INFO, format=f'[%(asctime)s] %(message)s', datefmt='%H:%M:%S')

logging.info('Starting Dreamlike Grouped')

logging.info('Loading MagicPrompt')
MagicPrompt=App.Interface.load('spaces/phenomenon1981/MagicPrompt-Stable-Diffusion')
def get_prompts(prompt_text):
    if prompt_text:
        return MagicPrompt('dreamlikeart, ' + prompt_text)
    else:
        return MagicPrompt('')
logging.info('loading Dreamlike Diffusion')
DreamDiffusion=App.Interface.load('models/dreamlike-art/dreamlike-diffusion-1.0') # Credits to Dreamlike
logging.info('Loading Dreamlike PhotoReal')
DreamPhotoReal = DreamDiffusion
#DreamPhotoReal=App.Interface.load('models/dreamlike-art/dreamlike-photoreal-2.0') # Credits to Dreamlike

def RestartScript():
    while True:
        RandomTime = random.randint(540, 600)
        time.sleep(RandomTime)
        logging.info('Restarting')
        os.execl(sys.executable, sys.executable, *sys.argv)

logging.info('Starting Auto-Restarter')
RestartThread = Thread(target=RestartScript, daemon=True)
RestartThread.start()

queue = Queue()
queue_threshold = 100

def AddNoise(Prompt, NoiseLevel=0.00):
    if NoiseLevel == 0:
        NoiseLevel = 0.00
    PercentageNoise = NoiseLevel * 5
    NumberNoiseCharacters = int(len(Prompt) * (PercentageNoise/100))
    NoiseIndices = random.sample(range(len(Prompt)), NumberNoiseCharacters)
    PromptList = list(Prompt)
    NoiseCharacters = list(string.ascii_letters + string.punctuation + ' ' + string.digits)
    NoiseCharacters.extend(['😍', '💩', '😂', '🤔', '😊', '🤗', '😭', '🙄', '😷', '🤯', '🤫', '🥴', '😴', '🤩', '🥳', '😔', '😩', '🤪', '😇', '🤢', '😈', '👹', '👻', '🤖', '👽', '💀', '🎃', '🎅', '🎄', '🎁', '🎂', '🎉', '🎈', '🎊', '🎮', '❤️', '💔', '💕', '💖', '💗', '🐶', '🐱', '🐭', '🐹', '🦊', '🐻', '🐨', '🐯', '🦁', '🐘', '🔥', '🌧️', '🌞', '🌈', '💥', '🌴', '🌊', '🌺', '🌻', '🌸', '🎨', '🌅', '🌌', '☁️', '⛈️', '❄️', '☀️', '🌤️', '⛅️', '🌥️', '🌦️', '🌧️', '🌩️', '🌨️', '🌫️', '☔️', '🌬️', '💨', '🌪️', '🌈'])
    for Index in NoiseIndices:
        PromptList[Index] = random.choice(NoiseCharacters)
    return ''.join(PromptList)

def GetRandomPrompt():
    with open('Prompts.txt', 'r') as Prompts:
        Prompts = Prompts.readlines()
        return random.choice(Prompts)

def FeedBack():
    logging.info('Good Feedback 😮')
    return

def SendIt1(Inputs, NoiseLevel, DreamDiffusion=DreamDiffusion):
    logging.info('Creating Image On 8 Threads')
    logging.info(f'Using Prompt: {Inputs}')
    logging.info('Creating Image On Thread 1')
    NoisedPrompt = AddNoise(Inputs, NoiseLevel)
    while queue.qsize() >= queue_threshold:
        time.sleep(2)
    queue.put(NoisedPrompt)
    Output1 = DreamDiffusion(NoisedPrompt)
    logging.info('Done Creating Image On Thread 1')
    return Output1

def SendIt2(Inputs, NoiseLevel, DreamDiffusion=DreamDiffusion):
    logging.info('Creating Image On Thread 2')
    NoisedPrompt = AddNoise(Inputs, NoiseLevel)
    while queue.qsize() >= queue_threshold:
        time.sleep(2)
    queue.put(NoisedPrompt)
    Output2 = DreamDiffusion(NoisedPrompt)
    logging.info('Done Creating Image On Thread 2')
    return Output2

def SendIt3(Inputs, NoiseLevel, DreamDiffusion=DreamDiffusion):
    logging.info('Creating Image On Thread 3')
    NoisedPrompt = AddNoise(Inputs, NoiseLevel)
    while queue.qsize() >= queue_threshold:
        time.sleep(2)
    queue.put(NoisedPrompt)
    Output3 = DreamDiffusion(NoisedPrompt)
    logging.info('Done Creating Image On Thread 3')
    return Output3

def SendIt4(Inputs, NoiseLevel, DreamDiffusion=DreamDiffusion):
    logging.info('Creating Image On Thread 4')
    NoisedPrompt = AddNoise(Inputs, NoiseLevel)
    while queue.qsize() >= queue_threshold:
        time.sleep(2)
    queue.put(NoisedPrompt)
    Output4 = DreamDiffusion(NoisedPrompt)
    logging.info('Done Creating Image On Thread 4')
    return Output4

def SendIt5(Inputs, NoiseLevel, DreamDiffusion=DreamDiffusion):
    logging.info('Creating Image On Thread 5')
    NoisedPrompt = AddNoise(Inputs, NoiseLevel)
    while queue.qsize() >= queue_threshold:
        time.sleep(2)
    queue.put(NoisedPrompt)
    Output5 = DreamPhotoReal(NoisedPrompt)
    logging.info('Done Creating Image On Thread 5')
    return Output5

def SendIt6(Inputs, NoiseLevel, DreamDiffusion=DreamDiffusion):
    logging.info('Creating Image On Thread 6')
    NoisedPrompt = AddNoise(Inputs, NoiseLevel)
    while queue.qsize() >= queue_threshold:
        time.sleep(2)
    queue.put(NoisedPrompt)
    Output6 = DreamPhotoReal(NoisedPrompt)
    logging.info('Done Creating Image On Thread 6')
    return Output6

def SendIt7(Inputs, NoiseLevel, DreamDiffusion=DreamDiffusion):
    logging.info('Creating Image On Thread 7')
    NoisedPrompt = AddNoise(Inputs, NoiseLevel)
    while queue.qsize() >= queue_threshold:
        time.sleep(2)
    queue.put(NoisedPrompt)
    Output7 = DreamPhotoReal(NoisedPrompt)
    logging.info('Done Creating Image On Thread 7')
    return Output7

def SendIt8(Inputs, NoiseLevel, DreamDiffusion=DreamDiffusion):
    logging.info('Creating Image On Thread 8')
    NoisedPrompt = AddNoise(Inputs, NoiseLevel)
    while queue.qsize() >= queue_threshold:
        time.sleep(2)
    queue.put(NoisedPrompt)
    Output8 = DreamPhotoReal(NoisedPrompt)
    logging.info('Done Creating Image On Thread 8')
    return Output8

logging.info('Loading Interface')
with App.Blocks(css='style.css') as demo:
    App.HTML(
        '''
            <div style='text-align: center; max-width: 650px; margin: 0 auto;'>
              <div>
                <h1 style='font-weight: 900; font-size: 3rem; margin-bottom:20px;'>
                  Dreamlike Grouped
                </h1>
              </div>
              <p style='margin-bottom: 10px; font-size: 96%'>
              Dreamlike Diffusion 1.0 | Dreamlike PhotoReal 2.0
              Noise Level: Controls how much randomness is added to the input before it is sent to the model. Higher noise level produces more diverse Outputs, while lower noise level produces similar Outputs,
                <a created by phenomenon1981</a>.
              </p>
              <p style='margin-bottom: 10px; font-size: 98%'>
              ❤️ Press the Like Button if you enjoy my space! ❤️</a>
              </p>
            </div>
        '''
    )
    with App.Column(elem_id='col-container'):
        with App.Row(variant='compact'):
            input_text = App.Textbox(
                label='Short Prompt',
                show_label=False,
                max_lines=4,
                placeholder='Enter a basic idea and click "Magic Prompt". Got no ideas? No problem, Simply just hit the magic button!',
            ).style(
                container=False,
            )
            output_prompt = App.Textbox(
                label='Random Prompt',
                show_label=False,
                max_lines=4,
                placeholder='Click "Random Prompt" to get a random prompt from a list!',
            ).style(
                container=False,
            )
            SeePrompts = App.Button('✨ Magic Prompt ✨').style(full_width=False)
            RandomPrompt = App.Button('🔄️ Random Prompt 🔄️').style(full_width=False)

        
        with App.Row(variant='compact'):
            prompt = App.Textbox(
                label='Enter your prompt',
                show_label=False,
                max_lines=4,
                placeholder='Full Prompt',
            ).style(
                container=False,
            )
            Run = App.Button('Generate Images').style(full_width=False)
        
        with App.Row():
            with App.Row():
                NoiseLevel = App.Slider(minimum=0.1, maximum=3, step=0.1, label='Noise Level', value=0.5)

        with App.Row():
            with App.Row():
                Output1=App.Image(label='Dreamlike Diffusion 1.0',show_label=True)
                Output2=App.Image(label='Dreamlike Diffusion 1.0',show_label=False)
                Output3=App.Image(label='Dreamlike Diffusion 1.0',show_label=False)
                Output4=App.Image(label='Dreamlike Diffusion 1.0',show_label=False)
                Output5=App.Image(label='Dreamlike PhotoReal 2.0',show_label=True)
                Output6=App.Image(label='Dreamlike PhotoReal 2.0',show_label=False)
                Output7=App.Image(label='Dreamlike PhotoReal 2.0',show_label=False)
                Output8=App.Image(label='Dreamlike PhotoReal 2.0',show_label=False)

        with App.Row():
            with App.Row():
                Feedback = App.Button('✅ Click here to send a positive feedback ✅')
        

        SeePrompts.click(get_prompts, inputs=[input_text], outputs=[prompt], queue=False)
        RandomPrompt.click(GetRandomPrompt, outputs=[prompt], queue=False)
        Run.click(SendIt1, inputs=[prompt, NoiseLevel], outputs=[Output1])
        Run.click(SendIt2, inputs=[prompt, NoiseLevel], outputs=[Output2])
        Run.click(SendIt3, inputs=[prompt, NoiseLevel], outputs=[Output3])
        Run.click(SendIt4, inputs=[prompt, NoiseLevel], outputs=[Output4])
        Run.click(SendIt5, inputs=[prompt, NoiseLevel], outputs=[Output5])
        Run.click(SendIt6, inputs=[prompt, NoiseLevel], outputs=[Output6])
        Run.click(SendIt7, inputs=[prompt, NoiseLevel], outputs=[Output7])
        Run.click(SendIt8, inputs=[prompt, NoiseLevel], outputs=[Output8])
        Feedback.click(FeedBack)


        with App.Row():
                App.HTML(    
    '''
        <div class='footer'>
        <p> Demo for <a href='https://huggingface.co/dreamlike-art/dreamlike-diffusion-1.0'>Dreamlike Diffusion 1.0</a> Stable Diffusion model
        <p> Demo for <a href='https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0'>Dreamlike PhotoReal 2.0</a> Stable Diffusion model
</p>
</div>
        <div class='acknowledgments' style='font-size: 115%'>
            <p> Unleash your creative side and generate mesmerizing images with just a few clicks! Enter a spark of inspiration in the 'Basic Idea' text box and click the 'Magic Prompt' button to elevate it to a polished masterpiece. Make any final tweaks in the 'Full Prompt' box and hit the 'Generate Images' button to watch your vision come to life. Experiment with the 'Noise Level' for a diverse range of Outputs, from similar to wildly unique. Let the fun begin!
            </p>
        </div>
    '''
)

    logging.info('Using Demo With 200 Concurrency Count')
    demo.launch(enable_queue=True, inline=True, share=False)
    block.queue(concurrency_count=300)
