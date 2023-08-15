import re

# The input text containing the play-by-play information
text = """
1stand 10 atQUE45 Queen's wins the toss, defers, Laurier to recieve
1st and 10 atQUE45 QUE ball on QUE4S.

Tyler Mullan kickoff 48 yards to the WLU17, Tyriq Quayson return 16 yards to the WLU33 (Jeremy Hiscox;R. Balogun.Jr).
Laurier at 15:00
stand 10 at WLU33 Taylor Elgersma pass complete to Ethan Jordan for loss of 4 yards to the WLU29 (Keegan Vanek).
2nd and 14 at WLU29 —_Taylor Elgersma pass complete to Ethan Jordan for 12 yards to the WLU41 (Eric Colonna).
3rd and 2 at WLU41 Dawson Hodge punt 45 yards to the QUE24, Aidan O'Neal return 6 yards to the QUE3O, out-of-bounds (Taylor Stalkie)
2 plays, 8 yards, 1:35 elapsed
Queen's at 13:25
Ist and 10 at QUE30 QUEEN'S drive start at 13:25.
stand 10 at QUE30 —_—Alex Vreeken pass incomplete to Richard Burton.
2nd and 10 at QUE30 —Alex Vreeken pass complete to Nathan Falconi for 26 yards to the WLUS4, 1ST DOWN QUE (Nico McCarthy).
stand 10 atWLUS4 —_Alex Vreeken pass complete to Richard Burton for 37 yards to the WLU17, 1ST DOWN QUE (M. Cote-Azore).
stand 10 atWLU17 —_-Yann Longa rush for 4 yards to the WLU13 (Damian Jamieson).
2nd and6 atWLU13 Alex Vreeken rush for 1 yard to the WLU12 (S. Hutchinson).
3rdand5atWLU12 —_—_Tyler Mullan field goal attempt from 19 GOOD, clock 11:03.

Queen's 3, Laurier 0
‘1st and Goal at QUE4S Change of possession, WLU ball on WLU35, 1st and 10.
6 plays, 68 yards, 2:22 elapsed
Laurier at 11:03
stand 10 at WLU35 —_LAURIER drive start at 11:03.
stand 10 atWLU35 Quentin Scott rush for 1 yard to the WLU36 (Eric Johnston;S. Seunarine)
2nd and9 at WLU36 —_—Taylor Elgersma pass incomplete to Ethan Jordan.
3rd and 9 at WLU36 Dawson Hodge punt 59 yards to the QUE15, out-of-bounds.
2 plays, 1 yards, 1:18 elapsed
Queen's at 09:45
Istand 10 atQUE15 QUEEN'S drive start at 09:45.
stand 10 atQUE15 Anthony Soles rush for 12 yards to the QUE27, 1ST DOWN QUE (Chris Haggart).
stand 10 at QUE27 — Anthony Soles rush for 8 yards to the QUE35.
2nd and2atQUE35 — Anthony Soles rush for 1 yard to the QUE36 (Ife Onyemenam).
3rd and 1 at QUE36 ‘Aayden Callan punt 39 yards to the WLU35, Nick Peterman retum 5 yards to the WLU40 (Jeremy Hiscox;Sam Csinos).
3 plays, 21 yards, 2:14 elapsed
Laurier at 07:31
stand 10 at WLU40 —_LAURIER drive start at 07:31.
stand 10 at WLU40 —_Taylor Elgersma pass incomplete to Tyriq Quayson
2nd and 10 at WLU40 Taylor Elgersma pass incomplete to Nick Peterman (Wells Karabin).
3rdand 10 at WLU40 Dawson Hodge punt 42 yards to the QUE28, Aidan O'Neal return 4 yards to the QUE32 (Ryan Speight;S. Hutchinson)
2 plays, 0 yards, 1:01 elapsed
Queen's at 06:30
Ist and 10 at QUE32_ QUEEN'S drive start at 06:30.
stand 10 at QUE32 —_—_Alex Vreeken pass incomplete to Nathan Falconi (S. Hutchinson)
2nd and 10 at QUE32 —_—Alex Vreeken pass incomplete to Liam Silverson, dropped pass.
3rd and 10 at QUE32_-—Aayden Callan punt 32 yards to the WLU46, Tyriq Quayson retum 7 yards to the WLUS3, PENALTY WLU illegal block 10 yards to the
2 plays, 0 yards, 1:05 elapsed
Laurier at 05:25
stand 10 at WLU43_ LAURIER drive start at 05:25.
stand 10 atWLU43 Quentin Scott rush for 3 yards to the WLU46 (S. Seunarine).
2nd and7 atWLU46 —_Taylor Elgersma sacked for loss of 6 yards to the WLU40 (Van Wishart).
3rd and 13 at WLU40 Dawson Hodge punt 49 yards to the QUE21, Aidan O'Neal return -1 yards to the QUE20 (Ryan Speight).
2 plays, -3 yards, 1:06 elapsed
Queen's at 04:19
Ist and 10 at QUE20 QUEEN'S drive start at 04:19.
stand 10 at QUE20 —_ Anthony Soles rush for no gain to the QUE20 (Jordan Veltri).
2nd and 10 at QUE20 —_Alex Vreeken pass incomplete to Aidan O'Neal.
3rd and 10 at QUE20 TEAM rush for loss of 20 yards to the QUEO, TEAM safety, clock 02:55.

Queen's 3, Laurier 2

1st and Goal at QUE35_—_ Change of possession, WLU ball on WLU35, 1st and 10.

 

3 plays, -20 yards, 1:24 elapsed
Laurier at 02:55
stand 10 atWLU35 —_ LAURIER drive start at 02:55.
stand 10 atWLU35 —_Taylor Elgersma pass complete to Raidan Thome for 6 yards to the WLU41.
2nd and4atWLU41 —_Taylor Elgersma pass complete to Ethan Jordan for 14 yards to the 55 yardline, 1ST DOWN WLU (Jared Siewe;Liam Sutherland).
stand 10 atWLUSS —_Taylor Elgersma pass incomplete to Tanner Nelmes.
2nd and 10 atWLUSS —_Taylor Elgersma pass incomplete to Raidan Thome (Wells Karabin).
3rdand 10 at WLUSS — Dawson Hodge punt 42 yards to the QUE13, Aidan O'Neal return 12 yards to the QUE25, out-of-bounds, PENALTY QUE holding 10 y:
plays, 20 yards, 2:11 elapsed
Queen's at 00:44
Istand 10 atQUE15 QUEEN'S drive start at 00:44.
stand 10 atQUE15 Anthony Soles rush for 14 yards to the QUE29, 1ST DOWN QUE (Nico McCarthy).
stand 10 at QUE29 —_—_Alex Vreeken pass complete to Nathan Falconi for 11 yards to the QUE40, 1ST DOWN QUE (Jordan Veltri;S. Hutchinson)
back to top
2nd

stand 10 at QUE40 _Start of 2nd quarter, clock 15:00.
stand 10 at QUE40 —Alex Vreeken pass incomplete to Aidan O'Neal (Brandon Omonuwa).
2nd and 10 at QUE40 — Alex Vreeken rush for 16 yards to the WLUS4, 1ST DOWN QUE (M. Cote-Azore).
stand 10 atWLUS4 —_Yann Longa rush for 7 yards to the WLU47, out-of-bounds (P. Burke Jr.)
2nd and 3 atWLU47 —-Yann Longa rush for 4 yards to the WLU43, 1ST DOWN QUE (Chisanem Nsitem;J. Fleurissaint).
stand 10 atWLU43 Alex Vreeken pass complete to Aidan O'Neal for loss of 1 yard to the WLU44 (Ryan Long).
2nd and 11 atWLU44 —_ Alex Vreeken pass incomplete to Ajang Chol.
3rdand11 at WLU44 —_Aayden Callan punt 37 yards to the WLU7, out-of-bounds.
8 plays, 51 yards, 3:53 elapsed
Laurier at 11:51
stand 10 at WLUO7 —_LAURIER drive start at 11:51.
stand 10 atWLUO7 — Quentin Scott rush for 11 yards to the WLU18, 1ST DOWN WLU, out-of-bounds (A. Miller-Melan).
stand 10 atWLU18 Quentin Scott rush for 2 yards to the WLU20 (Van Wishart;Eric Johnston).
2nd and8 atWLU20 _—_Taylor Elgersma pass complete to Ethan Jordan for 19 yards to the WLU39, 1ST DOWN WLU (Keegan Vanek).
stand 10 at WLU39 —_Taylor Elgersma pass incomplete to 6 (Wells Karabin).
2nd and 10 at WLU39_—_—Taylor Elgersma rush for 13 yards to the WLU52, 1ST DOWN WLU (Walter Karabin), PENALTY QUE OC 10 yards to the QUE48, 1ST I
stand 10 atQUE48 = Istand 10.
stand 10 at QUE48 —_—_Taylor Elgersma pass intercepted by S. Seunarine at the QUE43, S. Seunarine retum 0 yards to the QUE43.
6 plays, 55 yards, 2:41 elapsed
Queen's at 09:10
Ist and 10 at QUE43_ QUEEN'S drive start at 09:10.
stand 10 at QUE43 Jared Chisari rush for 11 yards to the QUES4, 1ST DOWN QUE (Ife Onyemenam)
stand 10 atQUE54 —_ Alex Vreeken pass complete to Nathan Falconi for 14 yards to the WLU42, 1ST DOWN QUE (Nico McCarthy), PENALTY WLU UR 15
stand 10 atWLU27 —Istand 10.
‘stand 10 at WLU27 —_Alex Vreeken pass incomplete to Aidan O'Neal, PENALTY QUE holding 10 yards to the WLU37, NO PLAY.
1st and 20 at WLU37 Jared Chisari rush for 23 yards to the WLU14, 1ST DOWN QUE, out-of-bounds (Nico McCarthy).
stand 10 atWLU14 —_Jared Chisari rush for loss of 1 yard to the WLU15 (J. Fleurissaint).
2nd and11atWLU15 Alex Vreeken pass complete to Nathan Falconi for 14 yards to the WLU1, 1ST DOWN QUE (J. Griffiths)
1st and Goal at WLUO1 Alex Vreeken rush for 1 yard to the WLUO, 1ST DOWN QUE, TOUCHDOWN, clock 05:39.

Tyler Mullan kick attempt good.

Queen's 10, Laurier 2
6 plays, 67 yards, 3:31 elapsed

Tyler Mullan kickoff 67 yards to the WLU-2, Tyriq Quayson return 26 yards to the WLU24 (Jared Chisari).
Laurier at 05:32
stand 10 at WLU24 —_ LAURIER drive start at 05:32.
stand 10 at WLU24 Tanner Nelmes rush for 1 yard to the WLU25, fumble by Tanner Nelmes recovered by QUE Liam Sutherland at WLU25.
1 plays, 1 yards, 0:36 elapsed
Queen's at 04:56
stand 10 atWLU25 QUEEN'S drive start at 04:56.
stand 10 atWLU25 —_—_Alex Vreeken pass complete to Richard Burton for 5 yards to the WLU20 (M. Cote-Azore).
2nd and 5 atWLU20 —_—_ Alex Vreeken pass incomplete to Josh Macleod.
3rdand5atWLU20 —_—_Tyler Mullan field goal attempt from 27 GOOD, clock 03:47.

Queen's 13, Laurier 2
‘1st and Goal at QUE4S Change of possession, WLU ball on WLU35, 1st and 10.
3 plays, 5 yards, 1:09 elapsed
Laurier at 03:47
stand 10 at WLU35 —_ LAURIER drive start at 03:47.
stand 10 atWLU35 —_Taylor Elgersma pass complete to Nick Petermann for 8 yards to the WLU43 (Darien Newell)
2nd and2atWLU43 Quentin Scott rush for 4 yards to the WLU47, 1ST DOWN WLU (Darien Newell).
stand 10 at WLU47 —_—_Raidan Thorne rush for 1 yard to the WLU48 (Eric Colonna;Walter Karabin).
2nd and 9 atWLU48 —_—Taylor Elgersma pass incomplete to Tyriq Quayson (A. Miller-Melan)
3rd and 9 at WLU48 Dawson Hodge punt 46 yards to the QUE16, Aidan O'Neal return 4 yards to the QUE20, PENALTY QUE illegal block 10 yards to the C
plays, 13 yards, 1:47 elapsed
Queen's at 02:00
Istand 10 atQUE10 QUEEN'S drive start at 02:00.
stand 10 atQUE10 —_-Yann Longa rush for 3 yards to the QUE13 (S. Hutchinson)
2nd and7 atQUE13 —_—_Alex Vreeken pass complete to Aidan O'Neal for 11 yards to the QUE24, 1ST DOWN QUE (P. Burke Jr.;S. Hutchinson)
‘stand 10 at QUE24 Yann Longa rush for 9 yards to the QUE33 (Jordan Veltri).
2nd and 1 at QUE33_ Yann Longa rush for no gain to the QUE33 (Luke Brubacher,J. Fleurissaint).
3rd and 1 at QUE33 Aayden Callan punt 40 yards to the WLU37, Nick Petermann return 8 yards to the WLU4S (Liam Sutherland)
A plays, 23 yards, 1:25 elapsed
Laurier at 00:35
stand 10 at WLU45 —_LAURIER drive start at 00:35.
stand 10 atWLU45 —_—_Taylor Elgersma rush for loss of 2 yards to the WLU43 (Liam Sutherland).
2nd and 12atWLU43 Taylor Elgersma pass complete to Nick Petermann for 9 yards to the WLUS2 (Liam Sutherland;Darien Newell)
3rd and 3 at WLUS2 Timeout Queen's, clock 00:08.

3rd and 3 at WLUS2 Dawson Hodge punt 33 yards to the QUE25, out-of-bounds.

 

2 plays, 7 yards, 0:32 elapsed
Queen's at 00:03
Ist and 10 atQUE25 QUEEN'S drive start at 00:03.
stand 10 at QUE25 TEAM rush for loss of 1 yard to the QUE24.
2nd and 11 at QUE24 —_End of half, clock 00:00.
1 plays, -1 yards, 0:03 elapsed
back to top
3rd
2nd and 11 at QUE24 _ Start of 3rd quarter, clock 15:00, QUE ball on QUE45.
Tyler Mullan kickoff 50 yards to the WLU15, Tyriq Quayson return 23 yards to the WLU38 (Brady Spafford).
Laurier at 14:46
stand 10 at WLU38 —_LAURIER drive start at 14:46.
stand 10 at WLU38 —_Taylor Elgersma pass complete to Ethan Jordan for 13 yards to the WLUS1, 1ST DOWN WLU (Eric Colonna).
stand 10 atWLUS1 Taylor Elgersma pass complete to Raidan Thorne for 8 yards to the QUES1 (Jared Siewe)
2nd and 2 at QUES1 Tanner Nelmes rush for 5 yards to the QUE46, 1ST DOWN WLU (Wells Karabin).
stand 10 at QUE46 —_—Taylor Elgersma pass complete to Raidan Thorne for 8 yards to the QUE38 (Jared Siewe)
2nd and2atQUE38 Tanner Nelmes rush for no gain to the QUE38 (Darien Newell)
3rd and 2 at QUE38 Dawson Hodge field goal attempt from 45 MISSED, kick to QUE-3, clock 11:44, Aidan O'Neal return 18 yards to the QUES (Nick Pet
6 plays, 34 yards, 3:02 elapsed
Queen's at 11:44
Ist and 10 atQUE15 QUE ball on QUE20.
stand 10 at QUE20 —_Jared Chisari rush for 4 yards to the QUE24 (Brandon Omonuwa).
2nd and 6 atQUE24 —_Alex Vreeken pass incomplete to Nathan Falconi.
3rd and 6 at QUE24 ‘Aayden Callan punt 36 yards to the WLUSO, Tyriq Quayson return 4 yards to the WLUS4 (Jacob Jefferies).
2 plays, 4 yards, 1:21 elapsed
Laurier at 10:23
stand 10 atWLUS4 —_ LAURIER drive start at 10:23.
stand 10 atWLUS4 —_Taylor Elgersma pass complete to Raidan Thorne for 5 yards to the QUES1, out-of-bounds.
2nd and 5 at QUES1 Taylor Elgersma pass complete to Raidan Thorne for 11 yards to the QUE40, 1ST DOWN WLU.
stand 10atQUE40 —_—Taylor Elgersma pass complete to Ethan Jordan for 40 yards to the QUEO, 1ST DOWN WLU, TOUCHDOWN, clock 09:29.
Dawson Hodge kick attempt good.
Queen's 13, Laurier 9
3 plays, 56 yards, 0:54 elapsed
Dawson Hodge kickoff 60 yards to the QUES, Aidan O'Neal return 13 yards to the QUE18, PENALTY QUE holding 9 yards to the QUE
Queen's at 09:18
Ist and 10 at QUEO9 QUEEN'S drive start at 09:18.
stand 10 at QUEO9 —_Jared Chisari rush for 2 yards to the QUE11 (J. Griffiths).
2nd and 8 at QUE11 Alex Vreeken pass incomplete to Josh Macleod.
3rd and 8 at QUE11 TEAM rush for loss of 11 yards to the QUEO, TEAM safety, clock 07:59.
Queen's 13, Laurier 11
‘1st and Goal at QUE35 Change of possession, WLU ball on WLU35, 1st and 10.
3 plays, -9 yards, 1:19 elapsed
Laurier at 07:59
stand 10 atWLU35 —_ LAURIER drive start at 07:59.
stand 10 atWLU35 ‘Tanner Nelmes rush for 6 yards to the WLU41 (Walter Karabin)
2nd and 4 atWLU41 —_Taylor Elgersma pass complete to Raidan Thorne for 10 yards to the WLU51, 1ST DOWN WLU, out-of-bounds (D. Matthews-Rei).
stand 10 atWLUS1 ‘Tanner Nelmes rush for 16 yards to the QUE43, 1ST DOWN WLU (Joshua Mobain;Keegan Vanek).
stand 10 at QUE43 Tanner Nelmes rush for 3 yards to the QUE4O (Walter Karabin).
2nd and7 atQUE40 —_—Taylor Elgersma pass incomplete to Ryan Long.
3rd and 7 at QUE40 Dawson Hodge field goal attempt from 47 MISSED, kick to QUE-6, clock 05:25, Aidan O'Neal return 18 yards to the QUE12 (Ryan Sp
6 plays, 35 yards, 2:34 elapsed
Queen's at 05:25
Ist and 10 atQUE12 QUE ball on QUE20.
stand 10 atQUE20 —_Alex Vreeken pass complete to Nathan Falconi for 14 yards to the QUE34, 1ST DOWN QUE (Jordan Veltri)
‘stand 10 at QUE34 Anthony Soles rush for 5 yards to the QUE39 (M. Cote-Azore;P. Burke Jr.).
2nd and 5 at QUE39 —Alex Vreeken pass complete to Nathan Falconi for 11 yards to the QUESO (P. Burke Jr.), PENALTY QUE illegal block 10 yards to the (
2nd and 15 at QUE29 —_Alex Vreeken pass complete to Aidan O'Neal for 8 yards to the QUE37 (Ryan Long).
3rd and 7 at QUE37 ‘Aayden Callan punt 38 yards to the WLU35, Tyriq Quayson retum 6 yards to the WLU41 (Justin Pace).
3 plays, 17 yards, 2:30 elapsed
Laurier at 02:55
stand 10 at WLU41 —_—_LAURIER drive start at 02:55.
stand 10 atWLU41 Tanner Nelmes rush for 6 yards to the WLU47 (Owen Stewart).
2nd and4atWLU47 —_—_Taylor Elgersma sacked for loss of 9 yards to the WLU38 (Van Wishart).
3rd and 13 at WLU38._ Dawson Hodge punt 50 yards to the QUE22, Keegan Vanek return 3 yards to the QUE25 (S. Hutchinson;Ryan Speight).
2 plays, -3 yards, 1:09 elapsed
Queen's at 01:46
Ist and 10 at QUE25 QUEEN'S drive start at 01:46.
stand 10 at QUE25 —_Alex Vreeken pass incomplete to Josh Macleod.
2nd and 10 at QUE25 —_—Alex Vreeken pass complete to Nathan Falconi for 23 yards to the QUE48, 1ST DOWN QUE (Nico McCarthy).
stand 10 at QUE48 Yann Longa rush for 14 yards to the WLU48, 1ST DOWN QUE (Nico McCarthy).
stand 10 at WLU48 —_—_Alex Vreeken pass complete to Aidan O'Neal for 8 yards to the WLUAO, out-of-bounds (P. Burke Jr.)
back to top
4th
2nd and2atWLU40 _ Start of 4th quarter, clock 15:00.
2nd and2atWLU40 — Anthony Soles rush for 4 yards to the WLU36, 1ST DOWN QUE (Ife Onyemenam).
stand 10 atWLU36 —_Alex Vreeken pass complete to Josh Macleod for 7 yards to the WLU29 (Ryan Long).
2nd and 3 atWLU29 —_-Jared Chisari rush for 29 yards to the WLUO, 1ST DOWN QUE, TOUCHDOWN, clock 13:39.
Tyler Mullan kick attempt good.
Queen's 20, Laurier 11
7 plays, 85 yards, 3:07 elapsed
Tyler Mullan kickoff 60 yards to the WLUS, Tyriq Quayson return 13 yards to the WLU18 (Aidan Vint).
Laurier at 13:31
stand 10 atWLU18 —_LAURIER drive start at 13:31.
stand 10 atWLU18 Quentin Scott rush for 3 yards to the WLU21 (Van Wishart).
2nd and7 atWLU21 —_Taylor Elgersma pass complete to Tyriq Quayson for 5 yards to the WLU26 (Walter Karabin;Van Wishart).
3rd and 2 at WLU26 Dawson Hodge punt 36 yards to the QUE48, Aidan O'Neal return 12 yards to the WLUSO, PENALTY WLU UR 15 yards to the WLU35,
2 plays, 8 yards, 1:36 elapsed
Queen's at 11:55
stand 10 at WLU35 QUEEN'S drive start at 11:55.
stand 10 atWLU35 —_Alex Vreeken pass incomplete to Richard Burton.
2nd and 10 at WLU35 —_Alex Vreeken pass incomplete to Liam Silverson, PENALTY WLU CR 10 yards to the WLU25, 1ST DOWN QUE, NO PLAY.
stand 10 atWLU25 —_Jared Chisari rush for 6 yards to the WLU19, PENALTY WLU offside 5 yards to the WLU20, NO PLAY.
1st and 5 at WLU20 Alex Vreeken pass incomplete to Josh Macleod, PENALTY WLU offside 5 yards to the WLU15, 1ST DOWN QUE, NO PLAY.
stand 10 atWLU15 —_—_Alex Vreeken pass complete to Richard Burton for 13 yards to the WLU2, 1ST DOWN QUE (Nico McCarthy).
1st and Goal at WLU02 Anthony Soles rush for 2 yards to the WLUO, 1ST DOWN QUE, TOUCHDOWN, clock 09:44.
Tyler Mullan kick attempt good.
Queen's 27, Laurier 11
5 plays, 35 yards, 2:11 elapsed
Tyler Mullan kickoff 55 yards to the WLU10, Ethan Jordan return 12 yards to the WLU22 (Eric Colonna).
Laurier at 09:38
stand 10 at WLU22 LAURIER drive start at 09:38.
stand 10 atWLU22 Taylor Elgersma sacked for loss of 2 yards to the WLU20 (Van Wishart).
2nd and12atWLU20 Taylor Elgersma sacked for loss of 4 yards to the WLU16 (Darien Newell)
3rd and 16 at WLU16 Dawson Hodge punt 42 yards to the QUES2, Aidan O'Neal return 20 yards to the WLU38 (Dawson Hodge).
2 plays, -6 yards, 1:12 elapsed
Queen's at 08:26
stand 10 at WLU38 QUEEN'S drive start at 08:26.
stand 10 atWLU38 Yann Longa rush for loss of 1 yard to the WLU39 (P. Burke Jr;Nico McCarthy).
2nd and 11 at WLU39 —_Alex Vreeken pass complete to Ajang Chol for 30 yards to the WLU9, 1ST DOWN QUE (S. Hutchinson).
1st and Goal at WLU09 Yann Longa rush for loss of 4 yards to the WLU13 (Luke Brubacher,J. Fleurissaint).
2nd and Goal at WLU13 Yann Longa rush for 9 yards to the WLU4 (P. Burke Jr.)
3rd and Goal at WLU04 Tyler Mullan field goal attempt from 11 GOOD, clock 05:13.
Queen's 30, Laurier 11
‘1st and Goal at QUE4S Change of possession, WLU ball on WLU35, 1st and 10.
5 plays, 34 yards, 3:13 elapsed
Laurier at 05:13
stand 10 atWLU35 —_LAURIER drive start at 05:13.
stand 10 atWLU35 —_Taylor Elgersma pass complete to Ethan Jordan for 11 yards to the WLU46, 1ST DOWN WLU (Jared Siewe;Liam Sutherland).
stand 10 atWLU46 —_Taylor Elgersma pass complete to Tanner Nelmes for 7 yards to the WLUSS (Silas Hubert;Eric Colonna).
2nd and 3 atWLUS3 —_Taylor Elgersma pass complete to Ethan Jordan for 4 yards to the QUES3, 1ST DOWN WLU (Liam Sutherland).
stand 10 at QUE53 —_—Taylor Elgersma pass complete to Tanner Nelmes for 12 yards to the QUE41, 1ST DOWN WLU (0. Matthews-Rei).
stand 10 atQUE41 —_—_Taylor Elgersma pass incomplete to Ethan Jordan.
2nd and 10 at QUE41 —_Taylor Elgersma pass complete to Nick Petermann for 5 yards to the QUE36.
3rd and § at QUE36 Taylor Elgersma pass incomplete to Nick Petermann.
7 plays, 39 yards, 2:46 elapsed
Queen's at 02:27
Ist and 10 at QUE36 QUEEN'S drive start at 02:27.
stand 10 at QUE36 —_Jared Chisari rush for 2 yards to the QUE38 (Ife Onyemenam).
2nd and8 at QUE38 —_Jared Chisari rush for 18 yards to the WLUS4, 1ST DOWN QUE (Ryan Long), PENALTY WLU UR 15 yards to the WLU39, 1ST DOWN
stand 10 at WLU39 —Istand 10.
stand 10 at WLU39 —_Jared Chisari rush for 4 yards to the WLU3S (J. Griffiths).
2nd and6 atWLU35 —_—_Jared Chisari rush for 5 yards to the WLU30 (Ife Onyemenam).
3rd and 1 at WLU30 Yann Longa rush for 3 yards to the WLU27, 1ST DOWN QUE (Brandon Omonuwa)
stand 10 at WLU27 Yann Longa rush for 2 yards to the WLU25 (Ivan Xu).
2nd and 8 at WLU25 —_-Yann Longa rush for 2 yards to the WLU23 (P. Burke Jr.)
3rd and 6 at WLU23 TEAM rush for 1 yard to the WLU22.
8 plays, 52 yards, 2:27 elapsed
Laurier at 00:00
stand 10 at WLU22 LAURIER drive start at 00:00.

1st and 10 at WLU22 End of game, clock 00:00."""

# Define regular expressions for various patterns
pattern_play_info = re.compile(r'^\d+\s+[ODK]\s+-?\d+\s+\d+\s+(\w+)\s+([-\d]+)\s+(\d+)\s+(\w+)\s+(.*?)$')
pattern_yard_ln = re.compile(r'-?\d+')
pattern_dn_dist = re.compile(r'\d+')

# Initialize lists to store extracted information
plays = []

# Split the text into lines and process each line
lines = text.split('\n')
for line in lines:
    print(pattern_yard_ln.findall(line))
    match_play_info = pattern_play_info.match(line)
    if match_play_info:
        play_type = match_play_info.group(1)
        yard_ln = int(pattern_yard_ln.findall(line)[0])
        dn = int(pattern_dn_dist.findall(line)[0])
        dist = int(pattern_dn_dist.findall(line)[1])
        result = match_play_info.group(4)
        description = match_play_info.group(5)

        plays.append({
            "play_type": play_type,
            "yard_ln": yard_ln,
            "dn": dn,
            "dist": dist,
            "result": result,
            "description": description
        })

# Print extracted information
for play in plays:
    print(play)
