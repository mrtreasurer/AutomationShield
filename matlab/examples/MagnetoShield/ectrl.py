"""
    MATRICES FOR EXPLICIT MPC POLYTOPES AND CORRESPONDING PWA LAWS

 	The automatically generated set of matrices have been adapted from 
    the C code auto-generation routine of the Multi-Parametric Toolbox 3 
    MPT3) of Kvasnica et al. for  MATLAB. Please see http://www.mpt3.org 
    for more information. Please see the original "toC.m" for more details
    in the MPT3.

    The following C code has been slightly adapted to perform microcontroller
    architecture-specific changes for AVR and ARM Cortex-A devices.

    The list of changes from the original are as follows:
    - Changed "static" modifiers to "const" so microcontrollers will
    prefer to use ROM instead of RAM.
    - Added PROGMEM functionality for the AVR architecture, and calling
    the necessary headers.
    - Removed the possibility to use PWQ, this only handles PWA.
    - Removed matrix export for the tie-breaking function.

    Usage: include alongside with the empcSequential.h header to your
    example.

    This code snippet has been altered for the needs of the
    the AutomationShield hardware and software ecosystem. 
    Visit http://www.automationshield.com for more details.


    Copyright (C) 2005 by Michal Kvasnica (michal.kvasnica@stuba.sk) 
    Revised in 2012-2013 by Martin Herceg (herceg@control.ee.ethz.ch)
    Adapted for MCU use by Gergely Takacs in 2020 (gergely.takacs@stuba.sk)
"""

MPT_NR = 17
MPT_DOMAIN = 4
MPT_RANGE = 2
MPT_ABSTOL = 1.000000e-08

MPT_A = [
4.05992279111818e-03,	-9.99680752040164e-01,	-2.34253118421290e-02,	8.55370051149914e-03,	-7.07106781186547e-01,	
7.07106781186547e-01,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	-9.94724568400619e-01,	
-9.62353253021573e-02,	3.55217564907855e-02,	-4.42443879993892e-01,	8.96793157507504e-01,	2.25242733190199e-03,	
-6.10143250372133e-04,	0.00000000000000e+00,	9.94724568400619e-01,	9.62353253021573e-02,	-3.55217564907855e-02,	
-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	
-3.46572076090655e-03,	9.99686455956125e-01,	2.32941941914421e-02,	-8.50641372499287e-03,	4.05992279111818e-03,	
-9.99680752040164e-01,	-2.34253118421290e-02,	8.55370051149914e-03,	-7.07106781186548e-01,	7.07106781186548e-01,	
0.00000000000000e+00,	0.00000000000000e+00,	-9.00711234906947e-03,	9.97469311761846e-01,	-6.60950292885053e-02,	
2.46026649742009e-02,	-4.49368902159980e-01,	8.93344197139292e-01,	1.87491503422450e-03,	-4.68937846267619e-04,	
9.00711234906947e-03,	-9.97469311761846e-01,	6.60950292885054e-02,	-2.46026649742009e-02,	-1.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	-4.05992279111818e-03,	
9.99680752040164e-01,	2.34253118421290e-02,	-8.55370051149914e-03,	-2.76813376391935e-03,	9.99692677027593e-01,	
2.31402527241647e-02,	-8.45089561712663e-03,	0.00000000000000e+00,	-9.94724568400619e-01,	-9.62353253021573e-02,	
3.55217564907855e-02,	-4.46262698795171e-01,	8.94900963518480e-01,	1.33995685964173e-03,	-2.71428371483434e-04,	
0.00000000000000e+00,	0.00000000000000e+00,	-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	9.94724568400619e-01,	
9.62353253021573e-02,	-3.55217564907855e-02,	-4.93221666599651e-03,	9.99953351287152e-01,	-7.74764899202179e-03,	
2.99038851141015e-03,	9.00711234906946e-03,	-9.97469311761846e-01,	6.60950292885053e-02,	-2.46026649742009e-02,	
4.46535419347354e-03,	-9.99676646436636e-01,	-2.35147702215904e-02,	8.58596311162123e-03,	3.46572076090655e-03,	
-9.99686455956125e-01,	-2.32941941914421e-02,	8.50641372499287e-03,	-7.07106781186548e-01,	7.07106781186548e-01,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	-9.94724568400619e-01,	-9.62353253021573e-02,	
3.55217564907855e-02,	-4.42443879993892e-01,	8.96793157507504e-01,	2.25242733190199e-03,	-6.10143250372133e-04,	
0.00000000000000e+00,	9.94724568400619e-01,	9.62353253021573e-02,	-3.55217564907855e-02,	-1.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	-3.46572076090655e-03,	
9.99686455956125e-01,	2.32941941914421e-02,	-8.50641372499287e-03,	-7.07106781186547e-01,	7.07106781186547e-01,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	-9.94724568400619e-01,	-9.62353253021573e-02,	
3.55217564907855e-02,	-4.42443879993892e-01,	8.96793157507504e-01,	2.25242733190199e-03,	-6.10143250372133e-04,	
0.00000000000000e+00,	-9.98478096589267e-01,	-5.15664871250366e-02,	1.95547446175563e-02,	7.07106781186547e-01,	
-7.07106781186547e-01,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	9.94724568400619e-01,	
9.62353253021573e-02,	-3.55217564907855e-02,	4.42443879993892e-01,	-8.96793157507504e-01,	-2.25242733190199e-03,	
6.10143250372133e-04,	-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	-1.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	
-4.05992279111818e-03,	9.99680752040164e-01,	2.34253118421290e-02,	-8.55370051149914e-03,	-3.46572076090655e-03,	
9.99686455956125e-01,	2.32941941914421e-02,	-8.50641372499287e-03,	4.42443879993892e-01,	-8.96793157507504e-01,	
-2.25242733190199e-03,	6.10143250372133e-04,	-7.07106781186547e-01,	7.07106781186547e-01,	0.00000000000000e+00,	
0.00000000000000e+00,	-4.46262698795171e-01,	8.94900963518480e-01,	1.33995685964173e-03,	-2.71428371483434e-04,	
-4.47722056862789e-01,	8.94171292428354e-01,	1.59137266182825e-03,	-3.56550995436984e-04,	0.00000000000000e+00,	
0.00000000000000e+00,	-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
1.00000000000000e+00,	-4.42443879993892e-01,	8.96793157507504e-01,	2.25242733190199e-03,	-6.10143250372133e-04,	
4.49368902159979e-01,	-8.93344197139292e-01,	-1.87491503422450e-03,	4.68937846267619e-04,	0.00000000000000e+00,	
-9.94724568400619e-01,	-9.62353253021573e-02,	3.55217564907855e-02,	4.46262698795171e-01,	-8.94900963518480e-01,	
-1.33995685964173e-03,	2.71428371483434e-04,	-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	-1.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
9.94724568400619e-01,	9.62353253021573e-02,	-3.55217564907855e-02,	-4.93221666599651e-03,	9.99953351287152e-01,	
-7.74764899202179e-03,	2.99038851141015e-03,	-9.00711234906946e-03,	9.97469311761846e-01,	-6.60950292885053e-02,	
2.46026649742009e-02,	4.46535419347354e-03,	-9.99676646436636e-01,	-2.35147702215904e-02,	8.58596311162123e-03,	
2.76813376391935e-03,	-9.99692677027593e-01,	-2.31402527241647e-02,	8.45089561712663e-03,	-1.58693470580666e-02,	
9.84278362946505e-01,	-1.64918293939811e-01,	6.12064080246643e-02,	1.58693470580666e-02,	-9.84278362946505e-01,	
1.64918293939811e-01,	-6.12064080246643e-02,	0.00000000000000e+00,	0.00000000000000e+00,	-1.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	-1.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	-2.76813376391935e-03,	9.99692677027593e-01,	
2.31402527241647e-02,	-8.45089561712663e-03,	-4.46535419347354e-03,	9.99676646436636e-01,	2.35147702215904e-02,	
-8.58596311162123e-03,	0.00000000000000e+00,	-9.94724568400619e-01,	-9.62353253021573e-02,	3.55217564907855e-02,	
4.93221666599651e-03,	-9.99953351287152e-01,	7.74764899202179e-03,	-2.99038851141015e-03,	-4.46262698795171e-01,	
8.94900963518480e-01,	1.33995685964173e-03,	-2.71428371483434e-04,	0.00000000000000e+00,	0.00000000000000e+00,	
-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
1.00000000000000e+00,	-4.93221666599651e-03,	9.99953351287152e-01,	-7.74764899202179e-03,	2.99038851141015e-03,	
0.00000000000000e+00,	9.94724568400619e-01,	9.62353253021573e-02,	-3.55217564907855e-02,	1.58693470580666e-02,	
-9.84278362946505e-01,	1.64918293939811e-01,	-6.12064080246642e-02,	3.46572076090655e-03,	-9.99686455956125e-01,	
-2.32941941914421e-02,	8.50641372499287e-03,	4.05992279111818e-03,	-9.99680752040164e-01,	-2.34253118421290e-02,	
8.55370051149914e-03,	-7.07106781186548e-01,	7.07106781186548e-01,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	-9.94724568400619e-01,	-9.62353253021573e-02,	3.55217564907855e-02,	-4.42443879993892e-01,	
8.96793157507504e-01,	2.25242733190199e-03,	-6.10143250372133e-04,	7.07106781186548e-01,	-7.07106781186548e-01,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	9.94724568400619e-01,	9.62353253021573e-02,	
-3.55217564907855e-02,	4.42443879993892e-01,	-8.96793157507504e-01,	-2.25242733190199e-03,	6.10143250372133e-04,	
0.00000000000000e+00,	9.98478096589267e-01,	5.15664871250366e-02,	-1.95547446175563e-02,	-1.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
-1.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	3.46572076090655e-03,	-9.99686455956125e-01,	
-2.32941941914421e-02,	8.50641372499287e-03,	0.00000000000000e+00,	-9.94724568400619e-01,	-9.62353253021573e-02,	
3.55217564907855e-02,	7.07106781186547e-01,	-7.07106781186547e-01,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	9.94724568400619e-01,	9.62353253021573e-02,	-3.55217564907855e-02,	4.42443879993892e-01,	
-8.96793157507504e-01,	-2.25242733190199e-03,	6.10143250372133e-04,	0.00000000000000e+00,	0.00000000000000e+00,	
-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
-1.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	-3.46572076090655e-03,	9.99686455956125e-01,	
2.32941941914421e-02,	-8.50641372499287e-03,	-4.46535419347354e-03,	9.99676646436636e-01,	2.35147702215904e-02,	
-8.58596311162123e-03,	0.00000000000000e+00,	-9.94724568400619e-01,	-9.62353253021573e-02,	3.55217564907855e-02,	
4.93221666599651e-03,	-9.99953351287152e-01,	7.74764899202179e-03,	-2.99038851141015e-03,	4.46262698795171e-01,	
-8.94900963518480e-01,	-1.33995685964173e-03,	2.71428371483434e-04,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	
0.00000000000000e+00,	-4.93221666599651e-03,	9.99953351287152e-01,	-7.74764899202179e-03,	2.99038851141015e-03,	
0.00000000000000e+00,	9.94724568400619e-01,	9.62353253021573e-02,	-3.55217564907855e-02,	-1.58693470580666e-02,	
9.84278362946505e-01,	-1.64918293939811e-01,	6.12064080246642e-02,	2.76813376391935e-03,	-9.99692677027593e-01,	
-2.31402527241647e-02,	8.45089561712663e-03,	4.05992279111818e-03,	-9.99680752040164e-01,	-2.34253118421290e-02,	
8.55370051149914e-03,	-9.00711234906947e-03,	9.97469311761846e-01,	-6.60950292885054e-02,	2.46026649742009e-02,	
7.07106781186548e-01,	-7.07106781186548e-01,	0.00000000000000e+00,	0.00000000000000e+00,	9.00711234906947e-03,	
-9.97469311761846e-01,	6.60950292885054e-02,	-2.46026649742009e-02,	4.49368902159980e-01,	-8.93344197139292e-01,	
-1.87491503422451e-03,	4.68937846267619e-04,	0.00000000000000e+00,	0.00000000000000e+00,	-1.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	-1.00000000000000e+00,	
1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	1.00000000000000e+00,	-4.05992279111818e-03,	9.99680752040164e-01,	2.34253118421290e-02,	
-8.55370051149914e-03,	4.93221666599651e-03,	-9.99953351287152e-01,	7.74764899202179e-03,	-2.99038851141015e-03,	
0.00000000000000e+00,	-9.94724568400619e-01,	-9.62353253021573e-02,	3.55217564907855e-02,	-4.46262698795171e-01,	
8.94900963518480e-01,	1.33995685964173e-03,	-2.71428371483434e-04,	0.00000000000000e+00,	0.00000000000000e+00,	
-1.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	
0.00000000000000e+00,	9.94724568400619e-01,	9.62353253021573e-02,	-3.55217564907855e-02,	9.00711234906947e-03,	
-9.97469311761846e-01,	6.60950292885053e-02,	-2.46026649742009e-02,	4.42443879993892e-01,	-8.96793157507504e-01,	
-2.25242733190199e-03,	6.10143250372133e-04,	7.07106781186548e-01,	-7.07106781186548e-01,	0.00000000000000e+00,	
0.00000000000000e+00,	4.46262698795171e-01,	-8.94900963518480e-01,	-1.33995685964173e-03,	2.71428371483434e-04,	
4.47722056862789e-01,	-8.94171292428354e-01,	-1.59137266182825e-03,	3.56550995436984e-04,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
1.00000000000000e+00,	-4.42443879993892e-01,	8.96793157507504e-01,	2.25242733190199e-03,	-6.10143250372133e-04,	
-4.49368902159980e-01,	8.93344197139292e-01,	1.87491503422450e-03,	-4.68937846267619e-04,	3.46572076090655e-03,	
-9.99686455956125e-01,	-2.32941941914421e-02,	8.50641372499287e-03,	0.00000000000000e+00,	-9.94724568400619e-01,	
-9.62353253021573e-02,	3.55217564907855e-02,	7.07106781186548e-01,	-7.07106781186548e-01,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	9.94724568400619e-01,	9.62353253021573e-02,	-3.55217564907855e-02,	
4.42443879993892e-01,	-8.96793157507504e-01,	-2.25242733190199e-03,	6.10143250372133e-04,	0.00000000000000e+00,	
0.00000000000000e+00,	-1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	-1.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	1.00000000000000e+00,	-4.05992279111818e-03,	
9.99680752040164e-01,	2.34253118421290e-02,	-8.55370051149914e-03,	4.93221666599651e-03,	-9.99953351287152e-01,	
7.74764899202179e-03,	-2.99038851141015e-03,	0.00000000000000e+00,	-9.94724568400619e-01,	-9.62353253021573e-02,	
3.55217564907855e-02,	4.46262698795171e-01,	-8.94900963518480e-01,	-1.33995685964173e-03,	2.71428371483434e-04,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	-1.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	1.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	9.94724568400619e-01,	
9.62353253021573e-02,	-3.55217564907855e-02,	-9.00711234906946e-03,	9.97469311761846e-01,	-6.60950292885053e-02,	
2.46026649742009e-02 ]

MPT_B = [
-6.87276281768414e-04,	7.07106781186548e+03,	9.16406150170932e+02,	4.42443881845692e+03,	9.16410007763341e+02,	
1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	
-3.59298691441914e-04,	1.29652322016667e-03,	7.07106781186548e+03,	1.12428276047865e+03,	4.49440504051327e+03,	
1.12428444361320e+03,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	
1.00000000000000e+04,	6.87276281768414e-04,	-1.58796374091681e-03,	9.16409737561113e+02,	4.47150118590788e+03,	
1.00000000000000e+04,	1.00000000000000e+04,	-9.16406150170932e+02,	3.89458847096974e+02,	-1.12428276047865e+03,	
-1.40136872617989e-03,	3.59298691441914e-04,	7.07106781186548e+03,	9.16406150170932e+02,	4.42443881845692e+03,	
9.16410007763341e+02,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	
1.00000000000000e+04,	1.66363826525151e-03,	7.07106781186548e+03,	9.16409737561113e+02,	4.42443878401507e+03,	
4.41332097829562e+02,	7.07106781186548e+03,	9.16406420373161e+02,	4.42443881586276e+03,	1.00000000000000e+04,	
1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	
-1.29652322016667e-03,	-1.43058162324961e-03,	-4.42443878401508e+03,	7.07106781186548e+03,	4.47150118590788e+03,	
4.48310816473853e+03,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	4.42443881845692e+03,	
-4.49440504051327e+03,	-9.16406420373160e+02,	4.47150118590788e+03,	1.00000000000000e+04,	1.00000000000000e+04,	
1.00000000000000e+04,	9.16410007763341e+02,	-3.89461509184873e+02,	-1.12428444361320e+03,	1.20505303883869e-03,	
1.58796374091681e-03,	2.36623641110035e+03,	2.36623641110035e+03,	1.00000000000000e+04,	1.00000000000000e+04,	
1.00000000000000e+04,	1.00000000000000e+04,	1.84665956858877e-03,	1.40136872617989e-03,	9.16409737561113e+02,	
-3.89458847096974e+02,	4.47150118590788e+03,	1.00000000000000e+04,	1.00000000000000e+04,	3.89461726025792e+02,	
-9.16406150170932e+02,	-2.36623641110035e+03,	-1.66363826525151e-03,	-1.50774035245666e-03,	7.07106781186548e+03,	
9.16406150170932e+02,	4.42443881845692e+03,	7.07106781186548e+03,	9.16410007763341e+02,	4.42443878142092e+03,	
4.41332424731958e+02,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	
1.00000000000000e+04,	1.00000000000000e+04,	1.43058162324961e-03,	9.16409737561113e+02,	7.07106781186548e+03,	
9.16406420373161e+02,	4.42443881586276e+03,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	
1.00000000000000e+04,	1.00000000000000e+04,	5.92355333443819e-04,	-1.20505303883869e-03,	-9.16406420373161e+02,	
3.89461509184873e+02,	4.47150118590788e+03,	1.00000000000000e+04,	1.00000000000000e+04,	-3.89458630256056e+02,	
9.16410007763341e+02,	-2.36623641110035e+03,	-1.84665956858877e-03,	4.76059149478425e-04,	1.12428458071328e+03,	
7.07106781186548e+03,	1.12428262337857e+03,	4.49440504160314e+03,	1.00000000000000e+04,	1.00000000000000e+04,	
1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	1.50774035245666e-03,	-3.89461726025792e+02,	
9.16409737561113e+02,	4.47150118590788e+03,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	
-9.16406150170932e+02,	-1.12428458071328e+03,	4.42443881586276e+03,	7.07106781186548e+03,	4.47150118590788e+03,	
4.48310816647448e+03,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	-4.42443878142092e+03,	
-4.49440504160314e+03,	-5.92355333443819e-04,	9.16409737561113e+02,	7.07106781186548e+03,	9.16406420373161e+02,	
4.42443881586276e+03,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	1.00000000000000e+04,	
1.00000000000000e+04,	-4.76059149478425e-04,	3.89458630256056e+02,	-9.16406420373160e+02,	4.47150118590788e+03,	
1.00000000000000e+04,	1.00000000000000e+04,	9.16410007763341e+02,	-1.12428262337857e+03 ]

MPT_NC = [
11,	12,	7,	12,	15,	
9,	8,	10,	8,	15,	
12,	8,	12,	8,	9,	
11,	7 ]


MPT_F = [
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	-2.04653887006119e+01,	5.03922271915600e+03,	
1.18083061414618e+02,	-4.31177672096171e+01,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	2.77283629129636e+03,	2.68259989729200e+02,	-9.90183802201752e+01,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	-1.71321244067409e+01,	4.94175783703193e+03,	
1.15150371416010e+02,	-4.20498211614906e+01,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
-1.28461139314128e+05,	2.60378945108517e+05,	6.53979847754719e+02,	-1.77151726200195e+02,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	2.77283629129636e+03,	
2.68259989729200e+02,	-9.90183802201752e+01,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	-1.71321244067409e+01,	3.83543699585977e+03,	9.02185921602863e+01,	-3.29415723381977e+01,	
-8.05949740182084e+00,	2.91063265733062e+03,	6.73734806961867e+01,	-2.46050144530788e+01,	0.00000000000000e+00,	
2.77283629129636e+03,	2.68259989729200e+02,	-9.90183802201752e+01,	-1.71321244067409e+01,	3.47335212041576e+03,	
-2.69115684447046e+01,	1.03871568244694e+01,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	-1.71321244067409e+01,	
4.94175783703193e+03,	1.15150371416010e+02,	-4.20498211614906e+01,	0.00000000000000e+00,	2.77283629129636e+03,	
2.68259989729200e+02,	-9.90183802201752e+01,	-1.71321244067409e+01,	3.47335212041576e+03,	-2.69115684447046e+01,	
1.03871568244694e+01,	-2.04653887006119e+01,	5.03922271915600e+03,	1.18083061414618e+02,	-4.31177672096171e+01,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
2.77283629129636e+03,	2.68259989729200e+02,	-9.90183802201752e+01,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	-1.28461139314128e+05,	2.60378945108517e+05,	6.53979847754719e+02,	
-1.77151726200195e+02,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	2.77283629129636e+03,	
2.68259989729200e+02,	-9.90183802201752e+01,	0.00000000000000e+00,	0.00000000000000e+00,	0.00000000000000e+00,	
0.00000000000000e+00 ]


MPT_G = [
5.37660000000000e+00,	-4.62340000000000e+00,	1.91215572981032e+00,	-4.62340000000000e+00,	2.55452580515119e+06,	
-4.62340000000000e+00,	5.37660000000000e+00,	-2.84727598262477e+00,	-4.62340000000000e+00,	-4.62340000000000e+00,	
-1.28461139314128e+09,	-4.62340000000000e+00,	-2.55452580515119e+06,	-4.62340000000000e+00,	1.77635683940025e-15,	
-1.77635683940025e-15,	2.55452580515119e+06,	-1.35279544172938e+06,	5.37660000000000e+00,	5.37660000000000e+00,	
-4.62340000000000e+00,	2.44840527062965e+00,	-2.55452580515119e+06,	1.35279544172938e+06,	-2.22366580804131e+00,	
5.37660000000000e+00,	2.55452580515119e+06,	5.37660000000000e+00,	1.28461139314128e+09,	5.37660000000000e+00,	
-4.62340000000000e+00,	5.37660000000000e+00,	-2.55452580515119e+06,	5.37660000000000e+00 ]
