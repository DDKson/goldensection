# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

import streamlit as st
import matplotlib.pyplot as mplt
import math as mt
import numpy as np
st.title("hello")
side = st.container()


def goldensection(a, b, f, acc):
    def func(f, a):
        f_clean = f.replace("x", a)
        return eval(f_clean)
    a = float(a)
    b = float(b)
    acc = float(acc)
    """find local minimum using golden section method
    printing graph and updated interval after each iteration
    a: lower bound (numerical)
    b: upper bound (numerical)
    f: function (1 variable) (string)
    acc: accuracy
    return final interval"""
    x = np.linspace(a, b)
    f_val = eval(f)
    p = (3-mt.sqrt(5))/2
    iteration = 0
    while b-a > acc:
        iteration += 1
        st.title(f"iteration{iteration}")
        p = (3-mt.sqrt(5))/2
        m = a + p*(b-a)
        n = b - p*(b-a)
        if func(f, str(m)) < func(f, str(n)):
            b = n
        else:
            a = m
        mplt.plot(x, f_val)
        mplt.axvline(x = a)
        mplt.axvline(x = b, color = "r")
        plot = mplt.show()
        st.pyplot(plot)
        st.write(f"updated interval: {[a,b]}")
    return [a,b]
with side:
    f = st.sidebar.text_input("enter function:")
    a = st.sidebar.text_input("enter lower bound:")
    b = st.sidebar.text_input("enter upper bound:")
    acc = st.sidebar.text_input("enter accuracy:")
    if f and a and b:
        goldensection(a, b, f, acc) 
st.set_option('deprecation.showPyplotGlobalUse', False)