import streamlit as sl
import testfunction as tf

def get_heat():
    pass

sl.title("Air Welding Calculator")

sl.text_input(label="speed", key="speed", value=float(0))

speed = sl.session_state["speed"]
speed = float(speed)
got_heat = tf.hmaterial1055_3test2(speed)

sl.info(tf.hmaterial1055_3test2(speed))

sl.text_input(label="heat", key="heat", value=float(0))

heat = sl.session_state["heat"]
heat = float(heat)

sl.info(tf.smaterial1055_3test2(heat))



sl.session_state