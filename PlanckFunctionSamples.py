#Brady Elster - Planck Distributions at Various Temperatures
#last updated: 5/8/2021

#imports
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.tri as tri
#import matplotlib as mpl
#from matplotlib import cm
#from colorspacious import cspace_converter

specarraysize = 3448
crval1 = 3064.392
cdelt1 = 1.871606648122
l = np.arange(0.1, crval1+specarraysize*cdelt1, cdelt1)
#########################################################
#constants in cgs units to match data from telescope - I sometimes like to add spectra to this plot
h = 6.626e-27
c = 2.9979e+10
k = 1.38e-16

# Planck Function
def planck(wav, T):
    #convert angstroms to cm to match cgs units of data
    wav = wav / 100000000
    a = 2.0*h*c**2
    b = h*c/(wav*k*T)
    part1 = (a) / (wav**5)
    part2 = 1 / (np.exp(b) - 1.0)
    intensity = part1 * part2
    intensity = intensity / 5e+30
    return intensity

factor = 1e-16
#the /1e-16 is just to somewhat normalize the plot because of the units I have
#note sure how to get rid of the overflow error
intensity = []
for i in range(5):
    if i == 0:
        intensity += [planck(l, 5000.)/factor]
    if i == 1:
        intensity += [planck(l, 6000.)/factor]
    if i == 2:
        intensity += [planck(l, 7000.)/factor]
    if i == 3:
        intensity += [planck(l, 8000.)/factor]
    if i == 4:
        intensity += [planck(l, 9000.)/factor]
    if i == 5:
        intensity += [planck(l, 10500.)/factor]

#plotting customization
plt.figure(figsize =(3, 3)) #makes a 3x3 figure (in theory)

ax = plt.gca()
ax.xaxis.label.set_size(34)
ax.yaxis.label.set_size(34)

#using this as a way of making a custom border line width of my plot
#can customize for an outset and inset plot if needed
lnthick_inset = 1.5 
lnthick_outset = 1.5

#set border sizes (line widths = 1.5) for all 4 sides
ax.spines["top"].set_linewidth(lnthick_outset)
ax.spines["left"].set_linewidth(lnthick_outset)
ax.spines["right"].set_linewidth(lnthick_outset)
ax.spines["bottom"].set_linewidth(lnthick_outset)

plt.rcParams.update({'font.size': 25})
ax.tick_params(axis='both', labelsize=25, length=10, width=3)
plt.xticks(fontfamily='sans-serif')
plt.yticks(fontfamily='sans-serif')

#Set the colors of each line according to a color palette
#(viridis is colorblind friendly for all types of colorblindness)
n = 5
colors = plt.cm.viridis(np.linspace(0, 1, n))
labels = ["T=5000 K", "T=6000 K", "T=7000 K", "T=8000 K", "T=9000 K", "T=10500 K"]

#plot each line
for i in range(n):
    plt.plot(l, intensity[i], color=colors[i], lw=3, label=labels[i])

#axes labels, title, legend
plt.xlabel('$\lambda (\AA)$')
plt.ylabel('$R(\lambda)$ Arbitrary Units')
plt.title("Planck Function at Varying Temperatures")
plt.legend(loc="best", shadow = True, fontsize = "small")

#show the plot
plt.show()
#plt.savefig("test1.png")
#plt.savefig("C:/Users/kskbr/Downloads/PlanckSamples_v5.png")

#slashes have to be forward / for some reason-
#-gets annoying to keep editing paths to match that - idk if you have a way of fixing this too?