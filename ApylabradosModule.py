#Primera Clase
class Pawns():

    points = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,
              'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,
              'W':4,'X':8,'Y':4,'Z':10}

    def __init__(self):
        self.letters = []

    def addPawn(self, c):
        '''
        Agrega la ficha "c" al objeto pawn
        '''

        self.letters.append(c)

    def addPawns(self, c, n):
        '''
        Agrega la ficha "c" n veces al objeto pawn
        '''
        for i in range(n):
            self.addPawn(c)

    def createBag(self):
      '''
      Agrega al objeto pawn todas las fichas del juego
      '''

      import pandas as pd
      path = '/content/drive/MyDrive/Colab Notebooks/FroGames/Python A-Z/Proyecto_Final/bag_of_pawns.csv'
      bag = pd.read_csv(path)

      for i in bag.itertuples():
        self.addPawns(i[1],i[2])

    def takeRandomPawn(self):
      '''
      Devuelve una ficha aleatoria del objeto pawn y la elimina
      '''
      import numpy as np
      pawn = np.random.choice(self.letters)
      self.letters.remove(pawn)
      return pawn

    def getFrequency(self):
      '''
      Devuelve un objeto FrequencyTable con la cantidad de fichas
      del objeto pawn
      '''
      objetoft = FrequencyTable()
      for i in self.letters:
        objetoft.update(i)
      return objetoft

    def showPawns(self):
      '''
      Devuelve un diccionario con las frecuencias de cada ficha
      '''
      objetoft = self.getFrequency()
      return objetoft.showFrequency()

    def takePawn(self,c):
      '''
      Elimina la ficha "c" del objeto pawn
      '''
      self.letters.remove(c)

    def getTotalPawns(self):
      '''
      Devuelve la cantidad de fichas del objeto pawn
      '''
      return len(self.letters)

    @staticmethod
    def getPoints(c):
      '''
      Devuelve el numero de puntos que vale la ficha "c"
      '''
      return Pawns.points[c]

    @staticmethod
    def showPawnsPoints():
      '''
      Muestra en pantalla el valor de cada ficha
      '''
      print('Puntos Por Ficha\n')
      count = 1
      end = '      '
      for c in Pawns.points:
        p = Pawns.getPoints(c)
        print('{}: {}{}'.format(c,' ' if p<10 else '',p),end = end)
        count+=1
        end = '\n' if count%5 == 0 else '      '




#Segunda Clase
class Word():

    def __init__(self):
      self.word = []

    def __str__(self):
      w = ''
      for i in self.word:
        w += i
      return w

    def areEqual(self,w):
      '''
      Devuelve True si el objeto word es igual al objeto word "w" o False
      en caso contrario
      '''
      if self.word == w.word:
        return True
      return False

    def isEmpty(self):
      '''
      Devuelve True si el objeto word es vacío
      '''
      if len(self.word) == 0:
        return True
      return False

    @classmethod
    def readWord(cls):
      '''
      Devuelve un objeto word despues de que introduzcas un string por teclado
      '''
      palabra = input('Introduce una palabra: ').strip()
      w = cls()
      for p in palabra:
        w.word.append(p.upper())
      return w

    @staticmethod
    def readWordFromFile(f):
      '''
      Devuelve un objeto word leído de un archivo txt 'f' ya abierto
      '''
      w = Word()
      palabra = f.readline()
      for p in palabra[:-1]:
        w.word.append(p.upper())
      return w

    def getFrequency(self):
      '''
      Devuelve un objeto FrequencyTable con la cantidad de fichas
      del objeto word
      '''
      objetoft = FrequencyTable()
      for i in self.word:
        objetoft.update(i)
      return objetoft

    def getLengthWord(self):
      '''
      Devuelve la cantidad de fichas del objeto word
      '''
      return len(self.word)
    



#Tercera clase
class Dictionary():

    filepath = "/content/drive/MyDrive/Colab Notebooks/FroGames/Python A-Z/Proyecto_Final/dictionary.txt"

    @staticmethod
    def validateWord(word):
      '''
      Devuelve True si el objeto word pertenece al diccionario
      o False en caso contrario
      '''
      with open(Dictionary.filepath) as f:
        w = Word.readWordFromFile(f)

        while not w.isEmpty() and not word.areEqual(w):
          w = Word.readWordFromFile(f)

        if w.isEmpty() and not word.areEqual(w):
          print('La palabra no está en el diccionario')
          return False
        else:
          return True

    @staticmethod
    def showWords(pawns):
      '''
      Muestra en pantalla las posibles palabras que se pueden formar con
      el objeto pawn
      '''
      tf_pawns = pawns.getFrequency()
      with open(Dictionary.filepath) as f:
        w = Word.readWordFromFile(f)

        while not w.isEmpty():
          tf_w = w.getFrequency()
          if FrequencyTable.isSubset(tf_w,tf_pawns):
            print(w)
          w = Word.readWordFromFile(f)

    @staticmethod
    def showWordsPlus(pawns,c):
      '''
      Muestra en pantalla las posibles palabras que se pueden formar con
      el objeto pawn y con la ficha adicional "c"
      '''
      tf_pawns = pawns.getFrequency()
      tf_pawns.update(c)
      with open(Dictionary.filepath) as f:
        w = Word.readWordFromFile(f)

        while not w.isEmpty():
          if c in w.word:
            tf_w = w.getFrequency()
            if FrequencyTable.isSubset(tf_w,tf_pawns):
              print(w)
          w = Word.readWordFromFile(f)





#Cuarta Clase
class FrequencyTable():

    def __init__(self):
      import pandas as pd
      import numpy as np
      path = '/content/drive/MyDrive/Colab Notebooks/FroGames/Python A-Z/Proyecto_Final/bag_of_pawns.csv'
      bag = pd.read_csv(path)

      self.letters = bag['Letter'].values
      self.frequencies = np.zeros_like(self.letters)

    def showFrequency(self):
      '''
      Devuelve un diccionario con las frecuencias de cada ficha
      '''
      d = {}
      for i in range(len(self.letters)):
        if self.frequencies[i] != 0:
          d[self.letters[i]] = self.frequencies[i]
      print(d)

    @staticmethod
    def isSubset(objeto1,objeto2):
      '''
      Devuelve True si el objeto1 es subconjunto del objeto2
      o False en caso contrario (ambos objetos son FreqTab)
      '''
      return all(objeto1.frequencies<=objeto2.frequencies)

    def update(self,c):
      '''
      Incrementa en una unidad la frecuencia de la ficha "c"
      '''
      i = self.letters.tolist().index(c)
      self.frequencies[i] +=1

    def delete(self,c):
      '''
      Decrementa en una unidad la frecuencia de la ficha "c"
      '''
      i = self.letters.tolist().index(c)
      self.frequencies[i] -=1




#Quinta clase
class Board():

    score = 0

    def __init__(self):
      self.board = [[' ' for _ in range(15)] for _ in range(15)]
      self.totalWords = 0
      self.totalPawns = 0
      self.multiplier = [[(1,'') for _ in range(15)] for _ in range(15)]

    def setUpMultiplier(self):
      '''
      Metodo que modifica el atributo multiplier del objeto board con los
      multiplicadores correspondientes a cada casilla
      '''
      import pandas as pd
      file_path = '/content/drive/MyDrive/Colab Notebooks/FroGames/Python A-Z/Proyecto_Final/multiplier_board.csv'
      multipliers = pd.read_csv(file_path)

      for row in multipliers.itertuples():
        self.multiplier[row[1]][row[2]] = (row[3],row[4])

    def showBoard(self):
      '''
      Muestra en pantalla el tablero con todas las fichas que contenga
      '''

      import matplotlib.pyplot as plt
      import numpy as np
      import pandas as pd

      fig = plt.figure(figsize=(6,6))
      ax = fig.add_subplot(111)

      for x in range(16):
        ax.plot([x,x],[0,15],c = '#999999')
        ax.plot([0,15],[x,x],c = '#999999')

      ax.set_xlim(-1,16)
      ax.set_ylim(-1,16)
      ax.set_position([0,0,1,1])  #para que la fig ocupe toda la pantalla
      ax.set_axis_off()           #para quitar los ejes

      def generate_vertex(x,y):
        '''
        Función que recibe la coordenada del centro de un cuadrado y
        devuelve sus vertices
        '''
        vertex = np.array([[x-0.5,y-0.5],[x-0.5,y+0.5],[x+0.5,y+0.5],[x+0.5,y-0.5]])
        return vertex

      file_path = '/content/drive/MyDrive/Colab Notebooks/FroGames/Python A-Z/Proyecto_Final/xycolor_board.csv'
      xycolors = pd.read_csv(file_path)

      for row in xycolors.itertuples():
        polygon = plt.Polygon(generate_vertex(row[1],row[2]),color = row[3])
        ax.add_artist(polygon)

      for i in range(15):
        ax.text(i+0.25,15.5,f'{i:02d}',fontsize=12,c='navy')
        ax.text(15.5,i+0.35,f'{14-i:02d}',fontsize=12,c='navy')

        for j in range(15):
          ax.text(j+0.35,14-i+0.35,self.board[i][j],fontsize=17)

      ax.text(0,-1,f'Score: {Board.score}',fontsize=17,c='navy')

      deal7Pawns()
      pawn_pos = 5

      for pawn in player_pawns.letters:
        polygon = plt.Polygon(generate_vertex(pawn_pos,-0.8),color="#FFF380")
        ax.add_artist(polygon)
        ax.text(pawn_pos,-0.6,pawn,va='center',ha='center',fontsize=17)
        pawn_pos +=1.5
      plt.show()


    def placeWord(self,player_pawns,word,x,y,direction):
      '''
      Escribe sobre el tablero el objeto "word", escrito con las fichas del
      objeto "player_pawns", en la posición (x,y).
      direction = [H : Horizontal, V : vertical]
      '''

      word_points = 0
      word_multiplier = 1
      for w in word.word:
        if w != self.board[x][y]:
          self.board[x][y] = w
          player_pawns.takePawn(w)
          self.totalPawns+=1

          if self.multiplier[x][y][1] != 'w':
            word_points += Pawns.getPoints(w) * self.multiplier[x][y][0]
          else:
            word_points += Pawns.getPoints(w)
            word_multiplier *= self.multiplier[x][y][0]


        if direction == 'H':
          y+=1
        if direction == 'V':
          x+=1

      Board.score += word_points * word_multiplier
      self.totalWords+=1
      self.showBoard()

    def isPossible(self,word,x,y,direction):
      '''
      Devuelve una tupla (Bool,message) en caso de que el objeto "word" se
      pueda o no escribir en la posición (x,y).
      direction = [H : Horizontal, V : vertical]
      '''
      message = ''
      x_init = x
      y_init = y

        #comprobemos si la primera palabra pasa por el centro (7,7)
      if self.totalWords == 0:
        message = 'La palara no cruza por el centro del tablero'
        if direction == 'V':
          if y_init != 7:
            return (False,message)
          elif (x_init+word.getLengthWord()-1<7) or (x_init>7):
            return (False,message)
        if direction == 'H':
          if x_init !=7:
            return (False,message)
          elif (y_init+word.getLengthWord()-1<7) or (y_init>7):
            return (False,message)

        #comprobemos si la palabra no se sale del tablero
      else:
        message = 'La palabra se sale del tablero'
        if direction == 'H':
          if (y_init<0) or (y_init>14) or (y_init+word.getLengthWord()>15):
            return (False,message)
        if direction == 'V':
          if (x_init<0) or (x_init>14) or (x_init+word.getLengthWord()>15):
            return (False,message)

        #comprobemos si se utilizan fichas del tablero
        blanks = []
        for w in word.word:
          if self.board[x][y] == ' ':
            blanks.append(w)
          if direction == 'H':
            y+=1
          if direction == 'V':
            x+=1
        if len(blanks) == word.getLengthWord():
          return (False,'No se están utilizando fichas del tablero')

        #comprobemos si una casilla está ocupada por la misma letra
        x = x_init
        y = y_init
        for w in word.word:
          if self.board[x][y] != ' ' and self.board[x][y]!=w:
            return (False,'Hay una casilla ocupada con una ficha diferente')
          if direction == 'H':
            y+=1
          if direction == 'V':
            x+=1

        #comprobemos si se están colocando nuevas fichas
        x = x_init
        y = y_init
        board_pawns = []
        for w in word.word:
          if self.board[x][y] == w:
            board_pawns.append(w)
          if direction == 'H':
            y+=1
          if direction == 'V':
            x+=1
        if len(board_pawns) == word.getLengthWord():
          return (False,'No se han puesto nuevas fichas en el tablero')

        #comprobemos que no hay fichas adicionales a principio o final de la palabra
        x = x_init
        y = y_init

        if direction == 'V':
          if (x!=0 and self.board[x-1][y]!= ' ') or (x+word.getLengthWord()!=14 and self.board[x+word.getLengthWord()][y]!=' '):
            return (False,'Hay fichas adicionales a principio o final de la palabra')
        if direction == 'H':
          if (y!=0 and self.board[x][y-1]!= ' ') or (y+word.getLengthWord()!=14 and self.board[x][y+word.getLengthWord()]!=' '):
            return (False,'Hay fichas adicionales a principio o final de la palabra')
      return (True,'La palabra se puede colocar sobre el tablero')

    def getPawns(self,word,x,y,direction):
      '''
      Devuelve un objeto Word con las fichas necesarias para escribir el objeto
      "word" en la posición (x,y).
      direction = [H : Horizontal, V : vertical]
      '''
      needed_letters = Word()
      possible,message = self.isPossible(word,x,y,direction)
      if not possible:
        print(message)
      else:
        for w in word.word:
          if self.board[x][y] != w:
            needed_letters.word.append(w)
          if direction == 'H':
            y+=1
          if direction == 'V':
            x+=1
      return needed_letters

    def showWordPlacement(self,pawns,word):
      '''
      Muestra en pantalla las posibles posiciones en las que puedes escribir
      el objeto "word" con las fichas del objeto "pawns"
      '''
      for direction in ('V','H'):
        print('{}:'.format('Vertical' if direction == 'V' else 'Horizontal'))
        for i in range(15):
          for j in range(15):
            isPossible = self.isPossible(word,i,j,direction)[0]
            if isPossible:
              needed_pawns = self.getPawns(word,i,j,direction)
              if FrequencyTable.isSubset(needed_pawns.getFrequency(),pawns.getFrequency()):
                print('(x={} , y={})'.format(i,j))




#Funciones para arrancar el juego
def startGame():
  '''
  Función que inicializa todas las variables para iniciar una partida nueva
  '''

  #Declaramos las siguiente variables globales
  global end
  end = False
  global show_help
  show_help = True
  global show_help_plus
  show_help_plus = True

  #Creamos la bolsa de fichas para jugar
  global bag_of_pawns
  bag_of_pawns = Pawns()
  bag_of_pawns.createBag()

  #Creamos las fichas del jugador
  global player_pawns
  player_pawns = Pawns()

  #Creamos el tablero para jugar
  global board
  board = Board()
  Board.score = 0
  board.setUpMultiplier()

  #Mensaje de bienvenida
  welcome()
  instructions()
  deal7Pawns()
  board.showBoard()
  legend()


def welcome():
  '''
  Función que muestra la bienvenida al juego
  '''
  file_path = '/content/drive/MyDrive/Colab Notebooks/FroGames/Python A-Z/Proyecto_Final/welcome_message.txt'
  with open(file_path) as f:
    print(f.read())


def instructions():
  '''
  Función que muestra las instrucciones del juego
  '''
  file_path = '/content/drive/MyDrive/Colab Notebooks/FroGames/Python A-Z/Proyecto_Final/instructions_message.txt'
  with open(file_path) as f:
    print(f.read())
  print()


def deal7Pawns():
  '''
  Función que reparte 7 fichas
  '''
  message = 'Estas son tus fichas:\n'
  while player_pawns.getTotalPawns()<7:
    pawn = bag_of_pawns.takeRandomPawn()
    player_pawns.addPawn(pawn)


def show_options():
  '''
  Función que muestra qué opciones tiene el jugador antes de introducir la
  primera palabra
  '''
  file_path = '/content/drive/MyDrive/Colab Notebooks/FroGames/Python A-Z/Proyecto_Final/options_message.txt'
  global show_help
  print('\nQue te gustaría hacer? {}\n'.format('' if show_help else '(Introduce SHOWHELP para ver las opciones)'))
  if show_help==True:
    with open(file_path) as f:
      print(f.read())
    show_help = False

  input_message = input().upper()
  if input_message == 'SHOWHELP':
    show_help = True
    show_options()
  elif input_message == 'ENTERWORD':
    introduceWord()
  elif input_message == 'PAWNSPOINTS':
    print()
    Pawns.showPawnsPoints()
    print()
    show_options()
  elif input_message == 'HELPWORD':
    helpWithWords()
    print()
    show_options()
  elif input_message == 'HELPLEGEND':
    legend()
    print()
    show_options()
  elif input_message == 'QUIT':
    endGame()
  else:
    show_options()


def show_options_plus():
  '''
  Función que muestra qué opciones tiene el jugador despues de haber introducido
  la primera palabra
  '''
  file_path = '/content/drive/MyDrive/Colab Notebooks/FroGames/Python A-Z/Proyecto_Final/options_plus_message.txt'
  global show_help_plus
  print('\nYa introdujiste una palabra, ahora que te gustaría hacer? {}\n'.format('' if show_help_plus else '(Introduce SHOWHELP para ver las opciones)'))
  if show_help_plus:
    with open(file_path) as f:
      print(f.read())
    show_help_plus = False

  input_message = input().upper()
  if input_message == 'SHOWHELP':
    show_help_plus = True
    show_options_plus()
  elif input_message == 'ENTERPOSITION':
    introduceCoordinatesAndDirection()
  elif input_message == 'ENTERWORD':
    introduceWord()
  elif input_message == 'PAWNSPOINTS':
    print()
    Pawns.showPawnsPoints()
    print()
    show_options_plus()
  elif input_message == 'HELPWORD':
    helpWithWords()
    print()
    show_options_plus()
  elif input_message == 'HELPPOS':
    helpWithPosition()
    print()
    show_options_plus()
  elif input_message == 'HELPLEGEND':
    legend()
    print()
    show_options()
  elif input_message == 'QUIT':
    endGame()
  else:
    show_options_plus()


def helpWithWords():
  '''
  Función que muestra en pantalla las palabras que se pueden formar con las fichas del
  jugador y las fichas sobre el tablero
  '''
  print('Posibles palabras a formar:')
  if board.totalWords == 0:
    Dictionary.showWords(player_pawns)
  else:
    board_letters = []
    for i in range(15):
      for j in range(15):
        if board.board[i][j] != ' ' and board.board[i][j] not in board_letters:
          board_letters.append(board.board[i][j])
          Dictionary.showWordsPlus(player_pawns, board.board[i][j])


def helpWithPosition():
  '''
  Función que muestra en pantalla las posibles posiciones en las que se puede
  colocar una palabra sobre el tablero
  '''
  print('\nPosibles posiciones:\n')
  board.showWordPlacement(player_pawns,new_word)


def introduceWord():
  '''
  Función que permite introducir una nueva palabra y comprueba en el diccionario
  si dicha palabra es valida y si puede formarse con las fichas del jugador
  más las fichas sobre el tablero
  '''
  global new_word
  new_word = Word.readWord()
  new_word_ft = new_word.getFrequency()
  player_pawns_ft = player_pawns.getFrequency()
  is_valid = Dictionary.validateWord(new_word)

  if board.totalWords == 0:
    new_word_is_subset = FrequencyTable.isSubset(new_word_ft,player_pawns_ft)

  else:
    board_letters = []
    forcedBreak = False
    for i in range(15):
      if forcedBreak:
        break
      for j in range(15):
        if board.board[i][j] != ' ' and board.board[i][j] not in board_letters:
          board_letters.append(board.board[i][j])
          player_pawns_plus = player_pawns_ft
          player_pawns_plus.update(board.board[i][j])
          new_word_is_subset = FrequencyTable.isSubset(new_word_ft,player_pawns_plus)
          player_pawns_plus.delete(board.board[i][j])

          if new_word_is_subset:
            forcedBreak = True
            break
  if not is_valid or not new_word_is_subset:
    if not new_word_is_subset:
      print('No posees las fichas necesarias para armar esa palabra')
    show_options()
  else:
    show_options_plus()


def introduceCoordinatesAndDirection():
  '''
  Función para introducir la posición y la dirección de una palabra
  y comprobar si es valida dicha ubicación
  '''
  print('Introduce la fila:',end=' ')
  x = int(input())
  print('Introduce la columna:',end=' ')
  y = int(input())
  print('Introduce la dirección:',end=' ')
  direction = input().upper()

  while direction != 'V' and direction != 'H':
      print('\nSolo hay 2 posibles direcciones: [V : vertical, H : horizontal]')
      print('Introduce la dirección:', end=' ')
      direction = input().upper()

  possible,message = board.isPossible(new_word,x,y,direction)
  if not possible:
    print(message)
    show_options_plus()
  else:
    needed_pawns = board.getPawns(new_word,x,y,direction)
    if FrequencyTable.isSubset(needed_pawns.getFrequency(),player_pawns.getFrequency()):
      board.placeWord(player_pawns,new_word,x,y,direction)
    else:
      print('No dispones de las fichas suficientes')
      show_options_plus()

def legend():
  import matplotlib.pyplot as plt
  import numpy as np
  import pandas as pd

  def generate_vertex(x,y):
    '''
    Función que recibe la coordenada del centro de un cuadrado y
    devuelve sus vertices
    '''
    vertex = np.array([[x-0.2,y-0.3],[x-0.2,y+0.3],[x+0.2,y+0.3],[x+0.2,y-0.3]])
    return vertex

  fig = plt.figure(figsize=(6.04,0.6))
  ax = fig.add_subplot(111)
  ax.set_xlim(0,10)
  ax.set_ylim(-0.5,1.5)
  ax.set_position([0,0,1,1])
  ax.set_axis_off()

  colors = ["#CCF9FF","#CCCEFF","#FFCCCC","#B0C4DE"]
  legend_names = ['x2\nLetra','x2\nPalabra','x3\nLetra','x3\nPalabra']
  for i in range(4):
    polygon = plt.Polygon(generate_vertex(1 + 2*i,0.5),color=colors[i])
    ax.add_artist(polygon)
    ax.text(1.3+2*i,0,legend_names[i],fontsize=12)
  plt.show()

def endGame():
  '''
  Función para finalizar la partida
  '''
  print('\nHas finalizado el juego')
  global end
  end = True