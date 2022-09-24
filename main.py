
import streamlit as st
import random

st.set_page_config(page_title='ROCK PAPER SCISSOR by RSK',
                   layout='centered',
                   menu_items={
                        'About' : '**I am a CEO bitch !**'
                       })

if 'player' not in st.session_state:
    st.session_state.player = 'start-button'
    st.session_state.playerScore = 0
if 'computer' not in st.session_state:
    st.session_state.computer = 'start-button'
    st.session_state.computerScore = 0
if 'totalRound' not in st.session_state:
    st.session_state.totalRound = 100/2
if 'progBar' not in st.session_state:
    st.session_state.progBar = 0
if 'buttonDisable' not in st.session_state:
    st.session_state.buttonDisable = False
if 'celebrate' not in st.session_state:
    st.session_state.celebrate = False

st.markdown('''
<style>
.css-1xarl3l.e16fv1kl1 {
color : blue;
padding-left : 20px;
}
</style>
''',unsafe_allow_html=True)


st.markdown('''
<style>
.css-1cpxqw2.edgvbvh9 {
height : 77px;
font-size : 50px;
border : solid;
border-radius : 15px;
box-shadow : 2px 2px #aaaaaa;
margin-left : 17px;
}
</style>
''',unsafe_allow_html=True)

st.sidebar.markdown('''
<style>
.css-15tx938.effi0qh3 {
font-weight : bold;
font-size : 20px;
}
</style>
''',unsafe_allow_html=True)

st.sidebar.markdown('''
<h1 style='font-size:30px;font-weight:bold;'>
Rock Paper Scissor
<i style='font-size:15px;'>by RSK</i>
</h1>
<hr>
''',unsafe_allow_html=True)

st.markdown('''
<style>
.css-50ug3q.e16fv1kl3 {
font-size : 30px;
font-weight : bold;
padding-top : 5px;
padding-left : 90px;
}
</style>
''',unsafe_allow_html=True)

st.markdown('''
<style>
.css-1qrvfrg.edgvbvh9 {
font-weight : bold;
width : 100%;
height : 50px;
}
</style>
''',unsafe_allow_html=True)

def score():
    p = st.session_state.player
    c = st.session_state.computer
    if p == c :
        return None
    elif (p == "rock") and (c == "paper"):
        st.session_state.computerScore += 1
    elif (p == "rock") and (c == "scissor"):
        st.session_state.playerScore += 1
    elif (p == "paper") and (c == "rock"):
        st.session_state.playerScore += 1
    elif (p == "paper") and (c == "scissor"):
        st.session_state.computerScore += 1
    elif (p == "scissor") and (c == "rock"):
        st.session_state.computerScore += 1
    elif (p == "scissor") and (c == "paper"):
        st.session_state.playerScore += 1
def computer_move():
    x = ["rock", "paper", "scissor"]*5
    st.session_state.computer = random.choice(x)
def numInputButton():
    st.session_state.buttonDisable = True
def restart():
    global numOfRounds 
    st.session_state.buttonDisable = False
    st.session_state.player = 'start-button'
    st.session_state.computer = 'start-button'
    st.session_state.playerScore = 0
    st.session_state.computerScore = 0
    st.session_state.progBar = 0
    st.session_state.totalRound = 100/numOfRounds
def playerMove():
    if st.session_state.rock:
        st.session_state.player = 'rock'
    elif st.session_state.paper:
        st.session_state.player = 'paper'
    elif st.session_state.scissor:
        st.session_state.player = 'scissor'
    st.session_state.progBar += st.session_state.totalRound
    computer_move()
    score()
    if st.session_state.progBar >= 100:
        st.session_state.buttonDisable = True
        if st.session_state.playerScore > st.session_state.computerScore:
            st.balloons()
            st.session_state.player = 'win'
            st.session_state.computer = 'win'

        else :
            st.session_state.player = 'lose'
            st.session_state.computer = 'lose'

st.markdown('''
<hr>
<h1 style='text-align:center;font-size:70px;'>
ROCK PAPER SCISSOR
</h1>
<hr>
''',unsafe_allow_html=True) 

numOfRounds = st.sidebar.number_input('Enter number of rounds : ',
                                      min_value=2,
                                      step=1,on_change=numInputButton)


left, right , result = st.columns([2,2,1])
left.metric('YOU', f'{st.session_state.playerScore}')
right.metric('COM', f'{st.session_state.computerScore}')
result.markdown('''
<p style='font-weight:bold;font-size:30px;height:50px;padding-left:7px;'>
ROUND
</p>
''',unsafe_allow_html=True)
result.progress(int(st.session_state.progBar))
st.markdown('<hr>',unsafe_allow_html=True)
you, com , sc = st.columns([2,2,1])

you.image(f'{st.session_state.player}.png')
com.image(f'{st.session_state.computer}.png')

sc.button('\U0000270A', key='rock',on_click=playerMove,
          disabled=st.session_state.buttonDisable)
sc.button('\U0000270B', key='paper',on_click=playerMove,
          disabled=st.session_state.buttonDisable)
sc.button('\U0000270C', key='scissor',on_click=playerMove,
          disabled=st.session_state.buttonDisable)
st.markdown('<hr>',unsafe_allow_html=True)

st.sidebar.button('PLAY \U0001F503', on_click=restart)










