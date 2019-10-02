from bokeh.plotting import figure, output_file, show

xf = 0
yf = 0

clicksx = []
clicksy = []

for i in open('output_filtered.txt').readlines():

    x = int(i[4] + i[5], 16)
    if x >= 1 << 7: x -= 1 << 8

    y = int(i[6] + i[7], 16)
    if y >= 1 << 7: y -= 1 << 8

    xf += x
    yf += y

    clicked = i[2] + i[3]
    if (clicked == '81'):
        clicksx.append(xf)
        clicksy.append(yf)

output_file("line.html")

p = figure(plot_width=600, plot_height=600)

# add a circle renderer with a size, color, and alpha
p.circle(clicksx[0:int(len(clicksx))], clicksy[0:int(len(clicksy))], size=1, color="black")

p.y_range.start = -5000
p.y_range.end = 5000

p.x_range.start = -5000
p.x_range.end = 5000

show(p)
