import numpy as np
import random
import math as mth 
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import FuncAnimation
import matplotlib.patches as mpatches 
import matplotlib.patheffects as PathEffects

plt.rcParams.update({'font.size': 28})
plt.rcParams["font.family"] = "Franklin Gothic Medium"
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['text.color'] = 'paleturquoise'

Movies = ['The Theory of Everything', 'Moneyball', 'American Psycho', 'Inglorious Basterds', 
'Marriage Story', 'When Harry Met Sally', 'Ladybird', 'Ray', 'Ferris Buellers Day Off',
'American Beauty', 'Reservoir Dogs', 'Nightcrawler', 'The Machinist', 'About Time']

N_Movies = len(Movies) 

#Generate Random Number to be used as the angle
Random_Num = random.randint(20,100)
N_Steps = 5*Random_Num

#angle values
theta = np.linspace(0,Random_Num,N_Steps)
final = np.full(400, Random_Num, dtype=np.int)
theta = np.concatenate((theta,final))


fig,ax = plt.subplots()
N_Movies = np.ones(N_Movies)
p1, t1= ax.pie(N_Movies, labels = Movies, labeldistance = 0.6, wedgeprops = {"edgecolor":"k", 'linewidth': 5, 'antialiased': True }, rotatelabels =True,textprops = dict(ha="center", va="center"))

[_.set_path_effects([PathEffects.withStroke(linewidth=3, foreground = 'k')]) for _ in t1]
[t.set_zorder(-1) for t in t1] # change the z-order of the patches so that the
                               # 2nd pie-chart ends up below the first one

ring_colours = ['gold']
p2, t2 = ax.pie([1], colors = ring_colours, radius = 1.15, wedgeprops = {"edgecolor":"k", 'linewidth': 5, 'antialiased': True })

[p.set_zorder(-1) for p in p1] # change the z-order of the patches so that the
                               # 2nd pie-chart ends up below the first one
[p.set_zorder(-2) for p in p2] # change the z-order of the patches so that the
                               # 2nd pie-chart ends up below the first one

def get_arrow(i):
    x = 0
    y = 0
    u = 0.8*mth.cos(-theta[i])
    v = 0.8*mth.sin(-theta[i])
    return x,y,u,v

x = get_arrow(0)[0]
y = get_arrow(0)[1]
u = get_arrow(0)[2]
v = get_arrow(0)[3]

arrow = mpatches.FancyArrowPatch((x,y),(u,v), linewidth = 5, joinstyle = 'round', facecolor = 'gold', edgecolor = 'black', mutation_scale = 80)
arrow.set_arrowstyle("simple", head_length = 0.65, head_width = 0.65, tail_width = 0.35)
ax.add_patch(arrow)

ax.set_aspect("equal")

def update(i):
    global arrow
    arrow.remove()
    x = get_arrow(i)[0]
    y = get_arrow(i)[1]
    u = get_arrow(i)[2]
    v = get_arrow(i)[3]
    arrow = mpatches.FancyArrowPatch((x,y),(u,v), linewidth = 5, joinstyle = 'round', facecolor = 'gold', edgecolor = 'black', mutation_scale = 80)
    arrow.set_arrowstyle("simple", head_length = 0.65, head_width = 0.65, tail_width = 0.35)
    ax.add_patch(arrow)

fig.set_facecolor('lavender')
title = ax.set_title('Sporclets Movie Wheel of Fortune', fontsize = 100, color = 'midnightblue')
title.set_path_effects([PathEffects.withStroke(linewidth=5, foreground = 'k')])

ani = FuncAnimation(fig, update, frames=np.arange(0,len(theta)), interval = 10)

plt.show()









