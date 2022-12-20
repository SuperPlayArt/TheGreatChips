import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog
import os 
import datetime
from git import Repo
import re
import random
x = datetime.datetime.now()

GIT_LINK = r"C:\Users\trist\Documents\sps_master\superplayart.github.io"

class gui:


    def test():
        root = Tk(className=' The Great Chips')
        Label(root, text='Quelles est votre fichier ?', font=("Helvetica 10 bold"), background='#020022', foreground="white", padding="1px").grid(row=0)
        Label(root, text='Où le mettre ?', font=("Helvetica 10 bold"), background='#020022', foreground="white", padding="1px").grid(row=1)
        Label(root, text='Quelle est le lien de ton image (artimg) ?', font=("Helvetica 10 bold"), background='#020022', foreground="white", padding="1px").grid(row=2)
        Label(root, text='Quelle est le titre de ton article (h1) ?', font=("Helvetica 10 bold"), background='#020022', foreground="white", padding="1px").grid(row=3)
        Label(root, text='Quelle est le texte que tu veux mettre (p) ?', font=("Helvetica 10 bold"), background='#020022', foreground="white", padding="1px").grid(row=4)
        Label(root, text="Synopsis ?", font=("Helvetica 10 bold"), background='#020022', foreground="white", padding="1px").grid(row=5)
        Label(root, text="Qui est l'auteur de l'article ?", font=("Helvetica 10 bold"), background='#020022', foreground="white", padding="1px").grid(row=6)
        where2 = Entry(root)
        title = Entry(root)
        txt = Entry(root)
        synopsis = Entry(root)
        auteur = Entry(root)
        def voyagevoyage():
            commande.articleminia(title.get(), txt.get(), img(), where2.get(), open_win_diag(), auteur.get(), synopsis.get(), save())  
        def open_win_diag():
            file=filedialog.askopenfilename(initialdir="./", title="Choisissez votre fichier html !",filetypes= (("index.html","*.html"),("all files","*.*")))
            return file
        def img():
            file=filedialog.askopenfilename(initialdir="./", title="Choisissez une image d'illustration !",filetypes= (("Image super kool","*.png"),("all files","*.*")))
            return file
        def save():
            file=filedialog.askdirectory(initialdir="./", title="Choisissez où sera sauvegarder vos article !")
            return file
        where2.grid(row=1, column=2)
        title.grid(row=3, column=2)
        txt.grid(row=4, column=2)
        synopsis.grid(row=5, column=2)
        auteur.grid(row=6, column=2)
        X = ttk.Button(root,text="Créer l'article",command=voyagevoyage )
        X.grid(row=7, column=2)
        root.configure(bg='#020022')
        root.mainloop()

    def interface():
        root = Tk(className=' The Great Chips')

        menubar = Menu(root)

        def configuration():
            config_win = Toplevel(root)
            config_win.title(" Configuration - The Great Chips")
            Label(config_win, text='Quelles est votre configuration ?', padding="1px").grid(row=0)
            Label(config_win, text='Quelles est votre fichier html ?', padding="1px").grid(row=1)
            where = Entry(config_win)
            Label(config_win, text='Dans quelle endroit du html ?', padding="1px").grid(row=3)
            where_html = Entry(config_win)
            Label(config_win, text='Où sont généralement vos images ?', padding="1px").grid(row=5)
            img_loc = Entry(config_win)
            Label(config_win, text='Dans quelles endroit vos articles seront stockés ?', padding="1px").grid(row=7)
            art_loc = Entry(config_win)
            Label(config_win, text='Quelles est votre pseudo ?', padding="1px").grid(row=9)
            pseudo = Entry(config_win)
            where.grid(row=2, column=0)
            where_html.grid(row=4, column=0)
            img_loc.grid(row=6, column=0)
            art_loc.grid(row=8, column=0)
            pseudo.grid(row=10, column=0)
            def sav():
                commande.save(where.get(), where_html.get(), img_loc.get(), art_loc.get(), pseudo.get())
            save = ttk.Button(config_win, text="Save", command=sav)
            save.grid(row=11, column=0)



        def alert():
            print("jdsuikdjg")
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Configuration", command=configuration)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=root.quit)
        menubar.add_cascade(label="Fichier", menu=menu1)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="A propos", command=alert)
        menubar.add_cascade(label="Aide", menu=menu3)

        root.config(menu=menubar)
        root.mainloop()


class commande:

    def save(where, where_html, img_loc, art_loc, pseudo):
        with open("config.txt","r+") as File:
            File.write(f"{pseudo}, voici votre configuration !\n")
            File.write(f"url_file : {where}\n")
            File.write(f"file_loc_into : {where_html}\n")
            File.write(f"img_loc : {img_loc}\n")
            File.write(f"pseudo : {pseudo}\n")
    
    def loadconfig():
        with open("config.txt","r+") as File:
            for line in File:
                if line.__contains__("url_file")==True:
                    where = line
                    where = where.replace("url_file : ","")
                    print(where)
                if line.__contains__("file_loc_into")==True:
                    where_html = line
                    where_html = where.replace("file_loc_into : ","")
                    print(where_html)
                if line.__contains__("img_loc")==True:
                    img_loc = line
                    img_loc = where.replace("img_loc : ","")
                    print(img_loc)
                if line.__contains__("pseudo")==True:
                    pseudo = line
                    pseudo = pseudo.replace("pseudo : ","")
                    print(pseudo)
        print(where, where_html, img_loc, pseudo)
                    

    def log(activity):
        
        with open("log.txt","r+") as File:
            data = File.read()
            li = data.splitlines()
            index = li.index("LOG :")+1
            li.insert(index,f"{x.strftime('%d/%m/%Y %H:%M:%S')} - {activity}")
            File.seek(0)
            for item in li:
                File.writelines(item+'\n')



    def articleminia(title, content, img, where, filename, auteur, synopsis, artsv):
        if (where ==""):
            where =  "<body>"
        else:
            where =  where
        directory = filename.replace("index.html","")
        html = f"{artsv}/{x.strftime('%d%m%Y')}{random.randint(1, 1000)}.html"
        html = html.replace(directory,"./")
        img = img.replace(directory,"./")
        print(html)
        print(img)
        filename = repr(filename)
        filename = filename.replace("\'","")
        
        with open(filename, encoding='utf8') as fin, open('temp', 'w+', encoding='utf8') as fout:
            for line in fin:
                fout.write(line)
                if line.__contains__(where)==True:
                    next_line = next(fin)
                    fout.write(f"<!--Les lignes qui suit ont était écrite via TheGreatChips c'est pourquoi leurs placements est spécial-->\n")
                    fout.write(f"<div class='minia' id='{x.strftime('%d%m%Y')}.{title}'>\n")
                    fout.write(f"<img class='artimg' src='{img}' alt='{img}'>\n")
                    fout.write(f"<h1>{title}</h1>\n")
                    fout.write(f"<h6>Créé par {auteur} le {x.strftime('%d/%m/%Y à %H:%M')}</h6>\n")
                    fout.write(f"<p>{synopsis}</p>\n")
                    fout.write(f"<a class='miniabtn' href='{html}'>En savoir plus...</a>")
                    fout.write(f"</div>\n")
                    fout.write(next_line)
                    
        os.remove(filename)
        os.rename(r'temp', filename)
        commande.article(title, content, img,auteur,html,artsv, directory)
        commande.log(f"Miniature d'article créé avec succées ({filename} : {title},{where},{img},{content})")
        print("Votre café est prêt... euh non mais l\'article à bien était crée") 
        commande.git_push()

    def article(title, content, img, auteur,html,artsv,directory):
        template = f"{directory}/template.html"
        txt = "texte"
        titre ="titre"
        with open(html, "w+", encoding='utf8') as file, open(template, 'r+', encoding='utf8') as template:
            for line in template:
                file.write(line)
                if line.__contains__("meta name='viewport'")==True:
                    next_line = next(template)
                    file.write(f"<title>{title} - SPA</title>\n")
                    file.write(next_line)
                if line.__contains__(titre)==True:
                    next_line = next(template)
                    file.write(f"<h1>{title}</h1>\n")
                    file.write(f"<h6>Créé par {auteur} le {x.strftime('%d/%m/%Y à %H:%M')}</h6>\n")
                    file.write(next_line)
                if line.__contains__(txt)==True:
                    next_line = next(template)
                    file.write(f"<h2>{content}</h2>\n")
                    file.write(next_line)
                if line.__contains__("imgwxyz")==True:
                    next_line = next(template)
                    file.write(f"<img class='artimg' src='{img}' alt='{img}'>\n")
                    file.write(next_line)
    def git_push():
            try:
                repo = Repo(GIT_LINK)
                repo.git.add(all=True)
                repo.index.commit(f"{x.strftime('%d/%m/%Y à %H:%M')}")
                origin = repo.remote(name='origin')
                origin.push()
            except:
                print("ERRRRRRRRREURR")

