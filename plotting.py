from bokeh.plotting import figure
from bokeh.io import output_file, save, reset_output, show

def plot(plotValues):
	labelsXaxis = [item for item in plotValues]
	labelsYaxis = [plotValues[item] for item in plotValues]
	p = figure(x_range=labelsXaxis,width=1100,title="Protien Sequencing")
	p.vbar(x=labelsXaxis,top=labelsYaxis,width=0.4)

	# Set some properties to make the plot look better
	p.xgrid.grid_line_color = None
	p.y_range.start = 0
	output_file('inde.html')
	save(p)

from math import cos, sin
from bokeh.models import ColumnDataSource

def modify_doc(doc):
    p = figure(match_aspect=True)
    p.circle(x=0, y=0, radius=1, fill_color=None, line_width=2)
    
    # this is just to help the auto-datarange
    p.rect(0, 0, 2, 2, alpha=0)

    # this is the data source we will stream to
    source = ColumnDataSource(data=dict(x=[1], y=[0]))
    p.circle(x='x', y='y', size=12, fill_color='white', source=source)

    def update():
        x, y = source.data['x'][-1], source.data['y'][-1]
I know that procedure, i just wanted 
        # construct the new values for all columns, and pass to stream
        new_data = dict(x=[x*cos(0.1) - y*sin(0.1)], y=[x*sin(0.1) + y*cos(0.1)])
        source.stream(new_dtsata, rollover=8)

    doc.add_periodic_callback(update, 150)
    doc.add_root(p)
    
def streaming_update(**kwargs):
	print(kwargs)
	# p = figure(x_range=[item for item in dicton],width=1100,title="Protien Sequencing")
	# p.vbar([item for item in dicton],top=[],width=0.4)

if __name__ == '__main__':
	# plot({"A": 120, "T": 221, "G":101,"C":189})
	def print_values(**kwargs):
    	for key, value in kwargs.items():
        	print("The value of {} is {}".format(key, value))

	print_values(
	            name_1="Alex",
	            name_2="Gray",
	            name_3="Harper",
	            name_4="Phoenix",
	            name_5="Remy",
	            name_6="Val"
	        )