from manimlib.imports import *

#video first part- introduction : questions to answer and what is going to be shown
class Intro(Scene):
	def construct(self):
		# first animation - title
		text1 = Text('Vectors',font = 'Cambria Math')
		text1.set_color(RED)
		self.play(ShowCreation(text1))
		self.wait(1)
		#second animation - move title and show the first question
		text2 = Text('Vectors',font = 'Cambria Math') # text1 = text2 except the screen position
		text2.to_corner(corner = UP+LEFT)
		text2.set_color(RED)
		self.play(Transform(text1,text2))
		self.wait(1)
		#third animation - show first question
		text3 = Text('1.) What are they?',font = 'Cambria Math')
		self.play(ShowCreation(text3))
		self.wait(5)
		#fourth animation - replace first question with the second question
		text4 = Text('2.) What purpose they serve?',font = 'Cambria Math')
		text5 = Text('1.) What are they?',font = 'Cambria Math')
		text5.set_color(GRAY)
		text5.to_corner(UP)
		text5.scale(0.5)
		self.play(Transform(text3,text5),ShowCreation(text4))
		self.wait(5)
		#fifth animation - replace second question with the third question
		text6 = Text('3.) How to represent vectors?', font = 'Cambria Math')
		text7 = Text('2.) What purpose they serve?',font = 'Cambria Math')
		text7.set_color(GRAY)
		text7.to_corner(UP)
		text7.scale(0.5)
		text7.shift(DOWN*0.5)
		self.play(ShowCreation(text6),Transform(text4,text7))
		self.wait(5)
		#sixth animation - replace third question with the fourth question
		text8 = Text('4.) How can we work with vectors?',font = 'Cambria Math')
		text9 = Text('3.) How to represent vectors?', font = 'Cambria Math')
		text9.set_color(GRAY)
		text9.to_corner(UP)
		text9.scale(0.5)
		text9.shift(DOWN)
		self.play(ShowCreation(text8),Transform(text6,text9))
		self.wait(5)
		#final animation - gray the last text
		text10 = Text('4.) How can we work with vectors?',font = 'Cambria Math',color = GRAY)
		text10.scale(0.5)
		text10.to_corner(UP)
		text10.shift(DOWN * 1.5)
		self.play(Transform(text8,text10))
		self.wait()

class Section1(Scene):
	def construct(self):
		#show section title
		t1 = Text('1.) What are they?',color = RED,font = 'Cambia Math')
		self.play(ShowCreation(t1))
		self.wait(5)
		#some lil text
		t2 = Text('Common mathematical representation:',font = 'Cambia Math')
		t3 = Text('1.) What are they?',color = RED,font = 'Cambia Math')
		t3.to_corner(UP+LEFT)
		self.play(Transform(t1,t3),ShowCreation(t2))
		self.wait(5)
		#show first formula
		f1 = TexMobject(r'\vec{v}',r' = (',r' v_x',r' ,',r' v_y',r')\text{ : } ',r'v_x',r',',r'v_y',r' \in \mathbb{R}')
		f1.set_color_by_tex(r'\vec{v}',YELLOW)
		f1.set_color_by_tex('v_x',RED)
		f1.set_color_by_tex('v_y',GREEN)
		f1.shift(DOWN)
		self.play(ShowCreation(f1))
		self.wait(5)
		#adapt formula for 3D vectors
		f2 = TexMobject(r'\vec{v}',r' = (',r' v_x',r' ,',r' v_y',r',',r' v_z',r')\text{ : } ',r' v_x',r', ',r' v_y',r', ',r' v_z',r' \in \mathbb{R}')
		f2.set_color_by_tex(r'\vec{v}',YELLOW)
		f2.set_color_by_tex('v_x',RED)
		f2.set_color_by_tex('v_y',GREEN)
		f2.set_color_by_tex('v_z',BLUE)
		f2.shift(DOWN)
		self.play(Transform(f1,f2))
		self.wait(5)
		#adapt formula for 4D vectors
		f3 = TexMobject(r'\vec{v}',r' = (',r' v_x',r', ',r' v_y',r', ',r' v_z',r', ',r' v_w',r')\text{ : } ',r' v_x',r', ',r' v_y',r', ',r' v_z',r', ',r' v_w',r' \in \mathbb{R}')
		f3.set_color_by_tex(r'\vec{v}',YELLOW)
		f3.set_color_by_tex('v_x',RED)
		f3.set_color_by_tex('v_y',GREEN)
		f3.set_color_by_tex('v_z',BLUE)
		f3.set_color_by_tex('v_w',PURPLE)
		f3.shift(DOWN)
		self.play(Transform(f1,f3))
		self.wait(5)
		#adapt formula for N-dimensional vectors
		f4 = TexMobject(r'\vec{v_n}',r' = (',r'v_1',r'v_2',r'\dots',r'v_n',r')\text{ : } ',r'v_1',r'v_2',r'\dots',r'v_n',r' \in \mathbb{R}')
		f4.set_color_by_tex(r'\vec{v_n}',YELLOW)
		f4.set_color_by_tex('v_1',RED)
		f4.set_color_by_tex('v_2',GREEN)
		f4.set_color_by_tex('v_n',BLUE)
		f4.shift(DOWN)
		self.play(Transform(f1,f4))
		#fade out - finish showing first formula, latex compiling is slow :c
		self.wait(5)
		self.play(FadeOut(f1),FadeOut(t1),FadeOut(t2))

		#represent vectors as a array

		t4 = Text("Vectors as arrays in computer science",font = "Cambia Math",color = YELLOW)
		self.play(ShowCreation(t4))
		self.wait(5)
		t5 = Text("Vectors as arrays in computer science",font = "Cambia Math",color = YELLOW)
		t5.to_corner(UP+LEFT)
		t5.scale(0.5)
		t5.shift(LEFT)
		self.play(Transform(t4,t5))
		self.wait(1)
			

		sq_array = [Square(),Square(),Square(),Square(),Square(),Square()]
		num_array = [Text("1",font = "Cambia Math"),Text("1",font = "Cambia Math"),Text("2",font = "Cambia Math"),Text("3",font = "Cambia Math"),Text("5",font = "Cambia Math"),Text("8",font = "Cambia Math")]

		sq_arrl = len(sq_array)

		for x in range(0,sq_arrl,1):
			d = (5-x)*LEFT
			sq_array[x].shift(d)
			sq_array[x].set_color(WHITE)
			sq_array[x].set_fill(BLACK)
			sq_array[x].set_height( sq_array[x].get_height() / 2)
			num_array[x].shift(d+(LEFT*0.125)+UP*0.125)
			num_array[x].set_color(BLUE)
			self.add(sq_array[x])
			self.add(num_array[x])

		l1 = Line(sq_array[0].get_corner(UP+LEFT),sq_array[sq_arrl-1].get_corner(UP+RIGHT))
		br1 = Brace(l1,UP)
		t6 = br1.get_text("int a[6];")
		self.add(br1,t6);
		self.wait(2)
		t7 = br1.get_text("float a[6];")

		num_array2 = [Text("1.00",font = "Cambia Math"),Text("1.14",font = "Cambia Math"),Text("2.15",font = "Cambia Math"),Text("3.92",font = "Cambia Math"),Text("5.65",font = "Cambia Math"),Text("8.35",font = "Cambia Math")]

		#convert the array to a float array
		for x in range(0,sq_arrl,1):
			d = (5-x)*LEFT
			num_array2[x].shift(d+(LEFT*0.125)+UP*0.125)
			num_array2[x].set_color(BLUE)
			num_array2[x].scale(0.7)

		self.play(Transform(t6,t7),
			Transform(num_array[0],num_array2[0]),
			Transform(num_array[1],num_array2[1]),
			Transform(num_array[2],num_array2[2]),
			Transform(num_array[3],num_array2[3]),
			Transform(num_array[4],num_array2[4]),
			Transform(num_array[5],num_array2[5]))
		self.wait(5)

