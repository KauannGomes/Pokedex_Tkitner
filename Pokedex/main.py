from tkinter import * #type:ignore
from PIL import Image, ImageTk
#--------------------------------------------------------------------------------------
#root
root = Tk()
root.geometry('580x750')
root.configure(bg='#CB6263')
root.title('Pokedex')
root.resizable(False,False)
frame_mid = Frame(root,bg='#CB6263')
frame_bottom = Frame(root,bg='#CB6263')

ico = Image.open("/Users/Kauan/Desktop/Pokedex/img/icon.png")
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

name = StringVar()
description = StringVar()

type_ = StringVar()
weaknesses_ = StringVar()

#--------------------------------------------------------------------------------------
#func

#Set used pokemons

#pikachu
def def_pikachu():
        global new
        new = ImageTk.PhotoImage(Image.open('/Users/Kauan/Desktop/Pokedex/img/pikachu.png'))
        img_pokemon.configure(image=new)
        name.set('Pikachu')
        description.set('Quando está irritado, descarrega imediatamente a energia armazenada nas bolsas em suas bochechas.')
        type_.set('Tipo: Elétrico')
        weaknesses_.set('Fraqueza: Terra')
def def_pichu():
        global new
        new = ImageTk.PhotoImage(Image.open('/Users/Kauan/Desktop/Pokedex/img/pichu.png'))
        img_pokemon.configure(image=new)
        name.set('Pichu')
        description.set('Não é qualificado para armazenar energia elétrica. Qualquer tipo de choque faz com que ele descarregue energia espontaneamente')
        type_.set('Tipo: Elétrico')
        weaknesses_.set('Fraqueza: Terra')      
def def_raichu():
        global new
        new = ImageTk.PhotoImage(Image.open('/Users/Kauan/Desktop/Pokedex/img/raichu.png'))
        img_pokemon.configure(image=new)
        name.set('Raichu')
        description.set('Sua cauda descarrega eletricidade no solo, protegendo-o de choques.')
        type_.set('Tipo: Elétrico')
        weaknesses_.set('Fraqueza: Terra')

#Gengar

def set_gastly():
        global new
        new = ImageTk.PhotoImage(Image.open('/Users/Kauan/Desktop/Pokedex/img/gastly.png'))
        img_pokemon.configure(image=new)
        name.set('Gastly')
        description.set('Ele envolve seu oponente em seu corpo gasoso, enfraquecendo lentamente sua presa ao envenená-la através da pele.')
        type_.set('Tipo: Fantasma | Veneno')
        weaknesses_.set('Fraqueza: Terra | Psíquica | Fantasma | Escuridão')
def set_haunter():
        global new
        new = ImageTk.PhotoImage(Image.open('/Users/Kauan/Desktop/Pokedex/img/hunter.png'))
        img_pokemon.configure(image=new)
        name.set('Haunter')
        description.set('Ele gosta de se esconder no escuro e bater nos ombros com a mão gasosa. Seu toque causa estremecimentos sem fim.')
        type_.set('Tipo: Fantasma | Veneno')
        weaknesses_.set('Fraqueza: Terra | Psíquica | Fantasma | Escuridão')    
def set_gengar():
        global new
        new = ImageTk.PhotoImage(Image.open('/Users/Kauan/Desktop/Pokedex/img/gengar.png'))
        img_pokemon.configure(image=new)
        name.set('Gengar')
        description.set('Para roubar a vida do seu alvo, ele se esconde na sombra da presa e espera silenciosamente por uma oportunidade.')
        type_.set('Tipo: Fantasma | Veneno')
        weaknesses_.set('Fraqueza: Terra | Psíquica | Fantasma | Escuridão')        

#charmander
def set_charmander():
        global new
        new = ImageTk.PhotoImage(Image.open('/Users/Kauan/Desktop/Pokedex/img/charmander.png'))
        img_pokemon.configure(image=new)
        name.set('Charmander')
        description.set('A chama em sua cauda mostra a força de sua força vital. Se Charmander estiver fraco, a chama também queimará fracamente.')
        type_.set('Tipo: Fogo')
        weaknesses_.set('Fraqueza: Água | Terra | Pedra ')        
def set_charmeleon():
        global new
        new = ImageTk.PhotoImage(Image.open('/Users/Kauan/Desktop/Pokedex/img/charmeleon.png'))
        img_pokemon.configure(image=new)
        name.set('Charmeleon')
        description.set('Quando ele balança sua cauda em chamas, a temperatura ao seu redor aumenta cada vez mais, atormentando seus oponentes.')
        type_.set('Tipo: Fogo')
        weaknesses_.set('Fraqueza: Água | Terra | Pedra ')        
def set_charizard():
        global new
        new = ImageTk.PhotoImage(Image.open('/Users/Kauan/Desktop/Pokedex/img/charizard.png'))
        img_pokemon.configure(image=new)
        name.set('Charizard')
        description.set('Se Charizard ficar realmente irritado, a chama na ponta de sua cauda queima em um tom azul claro.')
        type_.set('Tipo: Fogo | Voador')
        weaknesses_.set('Fraqueza: Água | Terra | Pedra ')        



#defining layout buttons
        

def click():

    name_pokemon_entry = text_entry.get().lower() 

    if name_pokemon_entry  == 'gastly':
          set_gastly()
    elif name_pokemon_entry == 'haunter':
          set_haunter()
    elif name_pokemon_entry == 'gengar':
          set_gengar()



    if name_pokemon_entry == 'pikachu':
        def_pikachu()  
    elif name_pokemon_entry == 'raichu':
        def_raichu()
    elif name_pokemon_entry == 'pichu':
         def_pichu() 

    if name_pokemon_entry == 'charmander':
          set_charmander()
    elif name_pokemon_entry == 'charmeleon':
          set_charmeleon()
    elif name_pokemon_entry == 'charizard':
          set_charizard()


def right_arrow():
    name_pokemon_entry = name_pokemon['text']

    if name_pokemon_entry == 'Gastly':
          set_haunter()
    elif name_pokemon_entry == 'Haunter':
          set_gengar()


    if name_pokemon_entry == 'Pikachu':
        def_raichu()
    elif name_pokemon_entry == 'Pichu':
         def_pikachu()


    if name_pokemon_entry == 'Charmander':
          set_charmeleon()
    elif name_pokemon_entry == 'Charmeleon':
          set_charizard()


def left_arrow():
    name_pokemon_entry2 = name_pokemon['text']

    if name_pokemon_entry2 == 'Haunter':
          set_gastly()
    elif name_pokemon_entry2 == 'Gengar':
          set_haunter()

          
    if name_pokemon_entry2 == 'Raichu':
        def_pikachu()
    elif name_pokemon_entry2 == 'Pikachu':
        def_pichu()


    if name_pokemon_entry2 == 'Charizard':
          set_charmeleon()
    elif name_pokemon_entry2 == 'Charmeleon':
          set_charmander()

#--------------------------------------------------------------------------------------
#Creating widgets


img_title = Image.open('/Users/Kauan/Desktop/Pokedex/img/pokemon.png')
photo_img = ImageTk.PhotoImage(img_title)

title_img = Label(root, image= photo_img,bg='#CB6263')


text_label = Label(frame_mid,text='Digite o nome do Pokémon:',font=('Arial',16),fg='#F8EE9C',bg='#CB6263')

text_entry = Entry(frame_mid,bg='#ffffff',fg='#000000',font=('Arial',12))
text_entry.focus()
btn = Button(frame_mid,text='Pesquisar',bg='#ffffff',fg='#000000',padx=10,pady=5,bd=0,command=click)

#pokemon info

name_pokemon = Label(frame_bottom,textvariable=name,bg='#CB6263',fg='#F8EE9C',font=('Arial',12))
desc = Label(frame_bottom,textvariable=description,wraplength=200,bg='#CB6263',fg='#F8EE9C',font=('Arial',12))
type_pokemon = Label(frame_bottom,textvariable=type_,bg='#CB6263',fg='#F8EE9C',font=('Arial',12))
Weaknesses = Label(frame_bottom,textvariable=weaknesses_,bg='#CB6263',fg='#F8EE9C',font=('Arial',12))


img_poke = ImageTk.PhotoImage(Image.open('/Users/Kauan/Desktop/Pokedex/img/pokedex.png'))
img_pokemon = Label(frame_bottom,image=img_poke,bg='#CB6263') 

img_arrow_right = Image.open('/Users/Kauan/Desktop/Pokedex/img/direita.png')
img_arrow_right = img_arrow_right.resize((50,50))
img_arrow_right = ImageTk.PhotoImage(img_arrow_right)


img_arrow_left = Image.open('/Users/Kauan/Desktop/Pokedex/img/esquerda.png')
img_arrow_left = img_arrow_left.resize((50,50))
img_arrow_left = ImageTk.PhotoImage(img_arrow_left)


btn_right = Button(root,image=img_arrow_right,bg='#CB6263',bd=0,command=right_arrow)
btn_left = Button(root,image=img_arrow_left,bg='#CB6263',bd=0,command=left_arrow)

#--------------------------------------------------------------------------------------
#Placing widgets in screen

title_img.grid(row=0,column=0,padx=40,pady=(20,50))



text_label.grid(row=2,column=0)
text_entry.grid(row=3,column=0,pady=(10,10))
btn.grid(row=4,column=0,pady=(5,40))
frame_mid.grid(row=1,column=0)


name_pokemon.grid(row=5,column=0,)
type_pokemon.grid(row=6,column=0,pady=10)
Weaknesses.grid(row=7,column=0,pady=(0,10))
desc.grid(row=8,column=0,)



btn_right.grid(row=10,column=0,padx=(100,0))
btn_left.grid(row=10,column=0,padx=(0,100)) 

img_pokemon.grid(row=9,column=0,)
frame_bottom.grid(row=2,column=0)

root.mainloop()


