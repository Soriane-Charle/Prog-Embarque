/************************************************************************/
/*				        	                        */
/*	  Pmod8LED Demo Project 		                        */
/*					    	                        */
/************************************************************************/
/*	Author: Eric Marsh					        */
/*	Copyright 2016, Digilent Inc.					*/
/************************************************************************/
/*  File Description: 			             		        */
/*					                        	*/
/* This file implements a simple demo application that demonstrates     */
/* how to setup and use the Pmod8LED.				        */
/*									*/
/*	Functionality:							*/
/*									*/
/* In the setup() function, the Pmod8LED is initialized through         */
/* calling the 8LED library.                                            */
/*                                                                      */
/*                                                                      */
/* In the loop() function, the application repeatedly tells the         */
/* microcontroller to tell the Pmod8LED to display several patterns.	*/
/*					       	                        */
/* This demo was tested with the JE port on the chipKit MX3             */
/*					       	                        */
/*	Required Hardware:		                                */
/*	  1. PIC32 based Microcontroller    	                        */
/*	  2. Pmod8LED                                             	*/
/*			                                                */
/************************************************************************/
/*  Revision History:			        			*/
/*					                        	*/
/*	8/8/2016(EricM): Created	       			        */
/*                                                                      */
/*					      	                        */
/************************************************************************/

/* -------------------------------------------------------------------- */
/*		        Include File Definitions                     	*/
/* -------------------------------------------------------------------- */
#include <WProgram.h>
#include "Eight_LED.h"

/* -------------------------------------------------------------------- */
/*		            Global Variables                     	*/
/* -------------------------------------------------------------------- */
eightLED my8LED;

/* -------------------------------------------------------------------- */
/*		            Function Definitions                     	*/
/* -------------------------------------------------------------------- */
void setup()
{
  // initialize pmod8LED. Pass the pin number connecting to the first LED.
  my8LED.begin(32);
}

void loop()
{
  // display several beautiful light patterns
  for(int i = 0; i < 4; i++){
    Checkered();
  }
  for(int i = 0; i < 4; i++){
    Wave();
  }
  for(int i = 0; i < 2; i++){
    Clap();
  }
}

// lights move in a wave pattern
void Wave(){
  for(int i = 0; i < 8; i++){
    my8LED.TurnOn(i);
    delay(20);
  }
  for(int i = 0; i < 8; i++){
    my8LED.TurnOff(i);
    delay(20);
  } 
}

// lights appear to 'clap' together
void Clap(){
  for(int i = 0; i < 4; i++){
    my8LED.Clear();
    my8LED.TurnOn(7 - i);
    my8LED.TurnOn(0 + i);
    delay(100);
  }
  for(int i = 3; i >= 0; i--){
    my8LED.Clear();
    my8LED.TurnOn(7 - i);
    my8LED.TurnOn(0 + i);
    delay(100);
  }
}

// lights turn on alternatingly
void Checkered()
{
  for(int i = 0; i < 8; i = i + 2){
    my8LED.TurnOn(i);
  }
  for(int i = 1; i < 8; i = i + 2){
    my8LED.TurnOff(i);
  }
  delay(300);

  for(int i = 0; i < 8; i = i + 2){
    my8LED.TurnOff(i);
  }
  for(int i = 1; i < 8; i = i + 2){
    my8LED.TurnOn(i);
  }
  delay(300);
}