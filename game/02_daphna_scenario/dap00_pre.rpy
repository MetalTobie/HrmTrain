################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label daphne_pre_01: #Снейп обещает, что пришлет шлюху

    $snape.State(pos2=gMakePos( 340, 420 )).Visibility("head", transition=None)
    $hero("Послушай, Северус. Ты уже давно обещал прислать мне парочку слизеринских шлюх.")
    $snape("~29// Гхм...")
    $hero("Что значит твое «гхм»?... Я точно знаю, у тебя есть шлюхи!// Ты сам мне недавно хвалился, что делаешь что угодно с кем захочешь.")
    $snape("~03// Понимаешь, мой друг, все не так просто.//~04// Эти девки... Они уверены, что ты,.. то есть директор, не в курсе наших маленьких шалостей.")
    $hero("И?")
    $snape("~03// И если окажется, что директору тоже не чуждо стремление к потас...\n к прекрасному, то это разрушит все их мировоззрение...")
    $hero("Послушай, дружище. Мне нет дела до мировоззрения шлюх, в них меня интересуют совсем другие детали.") 
    $snape("~06// Да, но если они узнают о твоем интересе, они могут не захотеть больше этим заниматься.//~16// #(Надеюсь, он проглотит эту хрень)//"
        "~29// #На самом деле, я не собираюсь присылать ему шлюх -//"
        " #Он же, мать его, джинн, обладающий крутой космической силой и все такое!//~26// #Кто знает, насколько он хорош в ЭТОМ.")
    $hero("Ты думаешь, я проглочу эту хрень?")
    $snape("~05//Хрень?//~04// Мой друг! Я о тебе забочусь! Они реально могут перестать давать!")
    $hero("Давать кому, дружище?// Не тебе ли?// Я думаю, тебе просто нравится быть единственным петухом в курятнике.//"
        "Я тут не досыпаю ночей, тружусь, чтобы выдрессировать тебе девчонку,...// а ты катаешься, как сыр в масле и не хочешь помочь мне немного развлечься.")
    $snape("~01// Да что тебя не устраивает?!// ~02//Я слышал, у вас очень хорошо продвигается с мисс Грейнджер.")
    $hero("Ты хочешь поменяться? Я готов уступить тебе воспитание этой девчонки всего за пару шлюх.") 
    $snape("~29// Эм...")
    $hero("Я тебя предупреждаю, Северус, если ты будешь и дальше утаивать от меня девок,..// директор может перестать скрываться в башне и выйдет сам на поиски!")
    $snape("~01// Но ты не можешь!..")
    $hero("Продолжай в том же духе и увидишь, могу я или нет...")
    $snape("~06//......")
    $hero("......")
    $snape("~02//............")
    $hero("............")
    $snape("~23// Ладно-ладно...// Ты меня убедил. Я пришлю тебе шлюху.")
    $hero("Двух шлюх, Северус.")
    $snape("~28// Я уверен, ЭТА тебе заменит двух сразу.")
    $hero("Смотри, если это окажется какая-то уродка...")
    $snape("~01// За кого ты меня принимаешь!// Чистая кровь в Мерлин знает каком поколении, была на обложке \"Ведьмополитен\"...//"
        "~02// #(стоит крайняя в пятом ряду)// ~01// ...чирлидерша, слизеринка, наконец!//"
        "~23// Девица - пальчики оближешь!")
    $hero("Ну, это ее забота... облизывать...// Так в чем подвох?")
    $snape("~05// Подвох?")
    $hero("Ты слишком быстро согласился. Вот я и спрашиваю: в чем подвох? ")
    $snape("~23// Никакого подвоха, мой друг!// ~02//Ты сам убедишься. Потерпи пару дней. Всего пару дней!")
    $snape.Visibility()
    "> Вы решаете довериться Снейпу и подождать два дня."
    "> Остаток вечера вы слушаете стенания Северуса\n о нелегкой доле преподавателя и\n фантазируете об обещанной шлюхе."

    $wtevent.Finalize("day_start")
#    jump day_start


label daphne_pre_02: #LV.1 (Whoring = 0 - 2)
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    $daphne.Visibility()
    menu:
        "\"Кто это?\"":
            $daphne(who, "Сэр, меня прислал профессор Снейп...")
            $hero("#(Превосходно! Шлюха прибыла!)// #(Надеюсь, она ничего. Впрочем, после стольких дней воздержания я не очень переборчив.)// Да, входи!")
        "\"Да, входи...\"":
            pass

#    dev "Жаль прерываться на самом интересном месте? "
#    dev "Нам тоже. Но данная сюжетная линия пока дописана только до этой точки..."
#    dev "(впрочем, вам доступны другие сюжетные линии)."
#    dev "Оставьте ваши вопросы, благодарности и пожелания на нашем {a=http://skazgames.com/forum/viewtopic.php?f=2&t=27}ФОРУМЕ{/a}. \nТак вы простимулируете нас и продолжение появится быстрее. :)"
    $daphne.LoadDefItemSets()
    $music("Daphne Theme")
#    $daphne.chibi.SetValue("appearance","a")
    $daphne.chibi.State("door", speed="go", appearance="a").Trans(d4, "blink").Trans("go center", "blink") # Если делать dissolve в движении, то сбивается счетчик времени. Лучше выполнить появление чибика стоя, затем уже двигать его 
    pause.5
    $screens.ShowD3("bld1")



    $daphne.State(pos="door").Visibility("body+")("~55 00 1 smi// Добрый день, профессор Дамблдор.") 
#    $hermi.Visibility("body+")(".....")

    $screens.Show("ctc").Pause().Hide("ctc")

    $hero  (m, "#(О-о, вот это шлюшка! Обожаю длинноногих блондинок!...)",g9,"#(...а также брюнеток, шатенок и рыжих. Я могу кончить от одного их вида!)",m," #(Вот только сиськи маловаты. Может, их подрастить заклинанием?..)", 
        g4, "#(Нет, джинни, умерь свои фантазии. Вспомни, что случилось, когда ты растил сиськи принцессе... мда)", 
        m, "Здравствуйте, мисс э-э...// #(Великие пески, почему он не назвал ее имени?).") 
    $daphne("~55 00 1 def// Профессор Снейп сообщил, что вы хотели меня видеть.") 
    $hero  ("О да, девочка! Несомненно, несомненно хотел... видеть, да.// Но, он же сказал, зачем тебя прислал?") 
    $daphne("~55 00 1 smi", "Нет, сэр. Он не сказал.") 
    $hero  ("#(Думаю, нужно с ней немного поболтать. Просто для разогрева.)") 

    menu: 
        "Поговорить насчет учебы": 
            $hero  ("Что ж, мисс, я хотел поговорить насчет вашей учебы.") 
            $daphne("Учеба не то, что меня волнует, сэр.// ~37 n0 1 def// Меня гораздо больше волнует, почему в Хогвартсе обучается грязнокровое мугродье.//" 
                "Вы же чистокровный волшебник, сэр?") 
            $hero  (g4, "Кто? Я?.. А, ну да. Вроде того.") 
            $daphne("~37 00 1 pur",  "Хм. Вы по делу смущаетесь.// По древности рода с Гринграссами никто не сравнится, вы и должны чувствовать себя неловко.") 
            $hero  (m,"#(Что это за... гринграссы такие?)// #(Как-то похабно рифмуется... Наверняка означает какую-нибудь дрянь.)") 
            $daphne("~37 00 1 pri",  "Но как бы то ни было, сэр. Мама говорит, вы должны были проследить, чтобы  мугродье не чувствовало себя здесь вольготно.", 
                "А вы вместо этого каждый год принимаете новых.//~46 01 1 neu// И чистокровные девочки должны испытывать сложности.") 
            $hero  ("Чистокровные девочки?") 
            $daphne("~26 00 1 neu",  "Да, сэр! Почему эту грязнокровку называют лучшей на курсе?//"
                "Почему мугродью разрешено учиться рядом с истинными волшебниками?//" 
                "~55 00 1 pri// Я могу еще быть рядом со всякими Малфоями или Паркинсон.//" 
                "Семейки так себе, второй сорт. Но какие-никакие чистокровки, а эта девица!!!") 
        "Поговорить насчет факультета": 
            $hero  ("Что ж, мисс, я хотел поговорить об обстановке на факультете.") 
            $daphne("~37 00 1 def",  "Обстановка на факультете, сэр? Она отвратительна!// Грязнокровое мугродье заполонило Хогвартс.") 
            $hero  ("#(Что это за?..)") 
            $daphne("~55 n0 1 ope",  "И вы делаете вид, что этого не замечаете. Хотя ваш отец...// Мама говорила мне, что он был истинным чистокровным волшебником и не побоялся прикончить троих маглов. За что его и упрятали в Азкабан.") 
            $hero  ("Правда, что ли? #(Ну и висельники в родстве с местным директором!)") 
            $daphne("~55 00 1 dis",  "Не притворяйтесь, что вы этого не помните, сэр!// А если позабыли, это не делает вам чести!", 
                "~55 00 1 pou// Гринграссы всегда стояли за чистоту крови, и когда видишь волшебника, который предает наши идеалы...") 

    $hero  ("#(Хм, какая экспрессия! Интересно, трахается она так же энергично?)// Постойте, мисс, это все очень увлекательно, но, может, уже завершим прелюдию и приступим?") 
    $daphne("~64 00 1 smi// Приступим к чему, сэр?") 
    $hero  ("Ну, к этому самому... чпоки-чпоки, тити-мити, а?") 
    $daphne("~64 w0 1 pur",  "\"Чпоки-чпоки\", сэр?") 
    $hero  ("Ну я не знаю, как это у вас, девушек, называется.// В общем, то, что вы постоянно делаете с профессором и зачем он вас сюда прислал.") 
    $daphne("~64 w0 1 pou// Я не понимаю, сэр.") 
    $hero  ("О, великие пески пустыни!// #(Она небыстро шевелит мозгами. Надеюсь, что бедрами шевелит быстрее.)//" 
        "Я говорю, заняться тем, чем обычно занимаются шлю... девчонки вроде вас.") 
    $daphne("~55 00 1 dis// На что это вы намекаете?!") 
    $hero  ("Я намекаю? Да я прямо говорю!...") 
    $daphne("~37 s0 1 dis",  "Если вы смеете намекать на то, чем занимаются некоторые особы с преподавателями, то это омерзительно!") 
    $hero  ("#(Э-э, Снейп, это что, шутка такая?)") 
    $daphne("~37 s0 1 ope",  "Я сегодня же пошлю сову родителям и сообщу о грязных предложениях, которые вы мне тут делаете.", 
        "А уж они донесут об этом в министерство, будьте уверены.") 
    $hero  (g4, "#(Не могу поверить!... Чертов Снейп!!!)// Эм, постойте, мисс, вы неправильно поняли!") 
    $daphne("~55 s0 1 dis// Я все правильно поняла! А вам недолго осталось сидеть в этом кресле!") 

    $music()
    $screens.HideD3("bld1")
    $daphne.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.5

    $hero("...................................")

    return wtevent.Finalize()

label daphne_pre_03: #Разборки со Снейпом после того, как шлюха оказалась не шлюхой

    $screens.Hide("snape_main")#.Pause(0.3)

    if not daytime:
        $hero(m, "Как тебе выпивка, дружище? Хорошо сидишь, удобно?// Тогда скажи...")
    $hero(g1, "Что это было?!.. Отвечай мне, во имя гребаных песков пустыни!")

    $snape.State("doorleft")("~01").Visibility("body" if daytime else "head")

    $snape("~05// Ты о чем, мой друг?")
    $hero("Не прикидывайся овечкой! Я просил у тебя шлюху, мать твою, а ты мне кого прислал?")
    $snape("~03// Ну, технически она шлюха.")
    $hero(m, "Что это вообще значит «технически она шлюха»?")
    $snape("~13// Ну, у нее есть все необходимое для шлюхи. Все нужные хм, детали. И какая экспрессия!")
    $hero("Да уж, экспрессию было трудно не заметить.")
    $snape("~20// Я бы ее с удовольствием разложил на полу.")
    $hero("Я бы тоже ее с удовольствием...",g4," Постой, так ты сам ни разу ее не трахнул?!")
    $snape("~02// За кого ты меня принимаешь, мой друг? Разве стал бы я предлагать тебе пользованный товар?// Чистокровная...")
    $hero(g4, "Про чистокровную я уже наслушался!")
    $snape("~23// Чистокровная нетронутая юная волшебница, которая только и ждет, чтобы кто-нибудь ее объездил.")
    $hero(m,"И ты решил, что я лучше всех подхожу на эту роль.")
    $snape("~02// Ну, у тебя неплохо получается с Гермионой Грейнджер. Я был уверен, что ты не спасуешь и перед Дафной Гринграсс.")
    $hero("Если бы ты, дружище, хотя бы предупредил меня, я бы может что-то и придумал.//"
        " Но теперь эта юная сука настучит родителям, и министерская проверка – самое меньшее, что нас ждет.//"
        "Предупреждаю, если меня вынесут из этого кабинета, то тебя вынесут следом #(если я не найду способа смыться раньше)")
    $snape("~06// Не все так трагично, мой друг. Я поговорил с мисс Гринграсс, и она согласна ничего не сообщать родителям.// Пока.")
    $hero("Слово «пока» особенно обнадеживает, гребаные пески...//"
        "Я не спрашиваю, как тебе это удалось. И все же, прости мое любопытство,..//"
        "...если ты так замечательно ладишь с этой сучкой,..// почему ты до сих пор ее не трахнул?!")
    $snape("~29// Мой друг. Одно дело убедить заносчивую дрянь в том, что шум вокруг такого деликатного предмета, как ее невинность, не в ее интересах.//"
        "И совсем другое - залезть к ней в трусики.// ~23// Я хочу предоставить эту честь тебе.")
    $hero("Не собираюсь я с ней больше встречаться!")
    $snape("~29// Боюсь, у тебя нет выбора.")
    $hero("Та-ак...// Чего я еще не знаю?")
    $snape("~10// Не хочу на тебя давить, мой друг.// Поэтому просто пусть события идут своим чередом. Может, все и обойдется.//"
        "Но на твоем месте я бы уже начал задумываться, как расположить к себе очаровательную девушку древнего и благородного рода.//"
        "~03// А теперь извини, мне пора идти.")

    $screens.Hide("snape_02", "bld1", d3 )
    $snape.Visibility(transition=d3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    $wtevent.Finalize("night_start" if daytime else "day_start")



label daphne_pre_05: #Разборки со Снейпом после письма от родителей Дафны, само письмо лежит в 15_mail:daphne_pre_04

    $screens.Hide("snape_main")#.Pause(0.3)

    if not daytime:
        $hero(m, "Не ожидал я от тебя, дружище...")
    $hero(m, "Ты опять меня подставил!")

    $snape.State("doorleft")("~01").Visibility("body" if daytime else "head")

    $snape("~05// Успокойся, мой друг, успокойся. Это было единственно возможным решением.")
    $hero("Да неужели?")
    $snape("~03// Конечно. Эти Гринграссы, эти снобы... Они уже были готовы забрать девчонку из Хогвартса.")
    $hero("Превосходно! Это решает все проблемы.")
    $snape("~01// Ты подумай, какова вероятность, что она наплетет про тебя, что было и чего не было, как только за ней закроется дверь.// И как они взбесятся. А уж связи у них. О-о... об этом можно книгу написать.// А пока она здесь...")
    $hero("Вот именно, она здесь и теперь может видеть меня каждый день.// Она тут кипела, как перегретый чайник! Думаешь, сразу все забудет?")
    $snape("~10// Кажется, ты потерял хватку, мой друг.// Важно не то, что она МОЖЕТ тебя видеть, а то, что она ОБЯЗАНА приходить к тебе, поскольку ей велели ее старики.//~20// Улавливаешь открывающиеся возможности?//"
        "До каникул она в полном твоем распоряжении, тебе дан «еще один шанс».// И я верю, что ты воспользуешься этим шансом на все 100%%.")
    $hero("Ты - чертов лицемер, Северус Снейп!// Я должен пыхтеть выдумывать, как обломать сразу двух девчонок, а ты в это время будешь развлекаться со шлюхами.")
    $snape("~02// Да, у каждого своя судьба, мой друг.")
    $hero(g4, "Ах, ты!.. Не ты ли все это устроил?")
    $snape("~09// Я всего лишь постарался исполнить твое желание наилучшим образом.// Если бы ты следовал нашему первоначальному плану и просто дрессировал мисс Грейнджер, ничего этого не случилось бы.//"
        "~06// Но тебе захотелось большего, мой друг, и я сделал все, что в моих силах.")
    $hero(m,"В твоих силах было прислать мне обычную шлюху!")
    $snape("~05// Чтобы на следующий день весь Хогвартс обсуждал, какой у директора размерчик?//"
        "~06// Эти шлюхи, когда их рот не занят полезным делом, только и делают, что болтают, и сплетня распространяется быстрее, чем действие заклинания икоты.//"
        "~13// Но если ты оприходуешь мисс Гринграсс, то можешь драть ее, как последнюю потаскуху, а за пределами твоего кабинета все будет тихо, чинно и благородно.//"
        "~22// Эта девица слишком помешана на своей голубой крови, чтобы признаться в том, что дает.")
    $hero("\"Если\" здесь ключевое слово, дружище. А если ничего не выйдет? Ты, кстати, так и не справился с ней.")
    $snape("~23// Гхм... Мой друг, я ведь не отказываюсь помочь тебе. Если тебе что-то нужно...")
    $hero(m,"Да, мне что-то нужно. Выкладывай о ней все, что знаешь!")
    $snape("~03// Это так скучно. Давай я лучше пришлю тебе сову с выписками из моего досье на нее.// Я его составлял, когда всерьез планировал ее завалить.//"
        "~04// И еще, думаю, тебе нужно почитать умных книжек, чтобы поучиться обращаться с девицами такого рода.// Опять же, есть специальное зелье...")
    $hero("Зелье?! А вот с этого момента поподробнее...")
    $snape("~06// Все в умных книгах, мой друг, все в них.")

    if not daytime:
        $snape("Давай не будем портить такой замечательный момент и просто выпьем.")
        "> Вы пытаетесь вытянуть из Снейпа что-то еще, но он только хлещет спиртное стаканами - похоже, студенты его всерьез достали."
        "> В конце концов он начинает кричать, что все, что ему нужно - это сигареты и алкоголь. Вы с трудом его утихомириваете и отправляете спать."
    else:
        $snape("У меня через 5 минут начинается зельеварение у Гриффиндора, так что я вынужден тебя оставить, мой друг.")



    $screens.Hide("snape_02", "bld1", d3 )
    $snape.Visibility(transition=d3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    $wtevent.Finalize("night_start" if daytime else "day_start")


label daphne_pre_07: #Разговор с Гермионой о Дафне. В зависимости от ветки и развращенности реакция. 
# После того, как будет получена информация о выпивке Дафны ивент заканчивается. А так с интервалом в 3 дня при попытке поговорить возобновляется.
    
    $hermi.State("door").Visibility("body+")
    $music("music/Chipper Doodle v2.mp3") # fadein 1 fadeout 1 # HERMIONE'S THEME.
    $hero  (m, "Я хотел бы поговорить с вами, мисс, о некоторых девушках с вашего факультета.//")
    if not wtevent.IsExec( 1, "start1"): # Если не прошел день с начала самого первого старта, т.е. это и есть первый старт
        $hermi("~body_04.png// О каких девушках?") 
        $hero  ("Да о всяких разных.") 
        $hermi("~body_06.png// Я не понимаю, сэр. На факультете много девушек.") 
        $hero  ("Да взять хотя бы первую, которая попадется. Кто у нас там первый...") 
        $hermi("~body_01.png// По алфавиту, сэр? Алисия.") 
        $hero  ("Причем здесь алфавит, великие пески! Первая девушка - совсем не эта...")
        $hermi("~body_84.png// О, сэр! Я поняла. Вы хотите поговорить обо мне, ведь я первая по успеваемости. Но вы стесняетесь...// Это... это так трогательно...") 
        $hero("Да нет же, нет! Это - Дафна Гринграсс.") 
        $hermi("~body_185.png// Я не понимаю, сэр. Почему это она - первая?") 
    else:
        $hermi("~body_09.png// Опять будете выспрашивать о Дафне?")

    $hero("Неважно, просто расскажи мне о ней.") 
    $hermi("~body_09.png// Хм...// Мне неприятно о ней говорить. Она все время кичится тем, что чистокровная.")
    $hero("Еще какие-нибудь сведения?") 
    $hermi("~body_03.png// Какого рода, сэр?")
    $hero("Ну может быть какие-нибудь... как бы получше выразиться... грешки?") 
    $hermi("~body_05.png// Сэр! Как вы можете требовать от меня рассказать такое про другую студентку! Это недостойно!")

    if hermi.whoring<12:
        $hermi("~body_04.png// Я немедленно ухожу!")
        $hermi.liking-=30
    else:
        $hero("Мисс Грейнджер, постойте. Примите во внимание, что Дафна - слизеринка, и предоставляя эту информацию, вы помогаете Гриффиндору.//"
            "Тем более, если у нее нет грешков, то вы ничего такого не сможете рассказать. А если есть - уж, наверное, она должна понести наказание.") 
        $hermi("~body_29.png// Все равно, сэр, это как-то...")
        if end.IsEnding(const_ENDING_STRONG_GIRL):
            $music("Supergirl")
            $hermi("~body_206.png// Все это напоминает методы ми-6, сэр, как показывают в сериалах. Вы случайно не работаете на спецслужбы?") 
            $hero  ("Очень смешно!") 
            $hermi("~body_186.png// Тогда посмейтесь, сэр. А я отправлю сову мистеру и миссис Гринграсс с письмом о том, что вы выведывали непристойную информацию об их дочери.") 
            $hero  (g4, "Постой! Кто говорит \"непристойную\"? Я не произносил этого слова!") 
            $hermi("~body_100.png// Вы не произносили, сэр. А я - произнесу.") 
            $hero  (m, "Во имя гребаных песков! Хорошо, я знаю, к чему ты клонишь. Ты хочешь еще очков?") 
            $hermi("~body_186.png// Десять очков, сэр...") 
            $hero  (g9, "Ха! Всего-то? Стоило огород городить.") 
            $hermi("~body_195.png// За каждое ее посещение.") 
            $hero  (g4, "Что? За каждое?... А если она... эмм...") 
            $hermi("~body_83.png// Если она так и не даст, сэр? Ну это уже не мои проблемы, правда? И еще 10%% со всех ваших доходов.") 
            $hero  (g4, "Великие пески! Зачем тебе деньги, девочка? Ты и так тут на полном пансионе!") 
            $hermi("~body_111.png// У меня ведь могут быть маленькие девичьи желания, правда?") 
            $hero  (m, "Мисс Грейнджер, в последнее время вы ведете себя...") 
            $hermi("~body_206.png// Вас что-то не устраивает в этом соглашении, сэр?")
            $hero  (m, "#Вот ведь мелкая шантажистка!") 
            $hermi("~body_186.png// Сэр?")

            menu: 
                "\".....Согласен!\"":
                    $hermi.SetValue("incomePercent",10)
                    $hermi.SetValue("pointsPerDaphneVisit",10)
                    $hero  ("В общем-то,.... устраивает. Хорошо, мисс Грейнджер, теперь рассказывайте.")
                    jump daphne_pre_06_OK

                "\"Подите прочь, мисс, с такими соглашениями!\"":
                    jump daphne_pre_06_Cancel

        else:
            $hermi("~body_29.png// Сэр, она вам нравится, да?")
            $hero("Не пори чушь, мне просто нужна информация.") 
            $hermi("~body_69.png// Я поражена, что вы обратили внимание на эту... на эту суку, сэр.//"
                " Она ходит, задрав нос, и не замечает никого, потому что ни у кого нет достаточно чистой крови.//"
                "~body_120.png// Странно, что она стала чирлидершей. Это же так низменно - полуодетой отплясывать перед толпой полукровок и грязнокровок.")
            $hero("Что еще?") 
            $hermi("~body_29.png// Все-таки она вам нравится...// ~body_50.png// Вы хотите познакомиться с ней поближе, сэр?")
            $hero("Что? Что ты несешь?!") 
            $hermi("~body_30.png// Я просто говорю то, что у вас на уме!//"
                "Это отвратительно, сэр, что вы хотите кое-чем заняться со своей студенткой. И где?! В этом самом кабинете, где...//")
            $hero("#...где все директора обычно и пялят студенток.") 
            $hermi("~body_191.png// Вы что-то сказали, сэр?")
            $hero("Не обращайте внимания. Но я ведь занимаюсь здесь кое-чем с вами, мисс Грейнджер. Это тоже отвратительно?") 
            $hermi("~body_206.png// Да, отвратительно, не думайте, что мне нравится!// Но это можно оправдать, это делается для блага гордого Гриффиндора!//"
                "~body_30.png// А тут вы просто хотите трахнуть эту... эту! Эту!!!...") 
            if hermi.liking>0:
                $hero("Мисс Грейнджер, вы ведь знаете, что я отличаю вас среди прочих студентов.")
                $hermi("~body_29.png// Я... я думаю это так, сэр. Но после того, что здесь происходит, как я могу вам доверять?") 
                $hero("Что вы имеете в виду, мисс?")
                $hermi("Вы знаете, сэр. Все эти лапания... и все остальное.") 
                $hero("Мисс Грейнджер...")
                $hermi("~body_50.png// Довольно, сэр. Я расскажу вам то, что вы хотите знать. Чтобы вы понимали, какая это дрянная девка.//"
                    "~body_61.png// Конечно, это ни на секунду вас не остановит...// Но у меня есть условие!") 
                $hero("................?")
                $hermi("~body_47.png// Эта девица не должна появляться здесь чаще, чем раз в два дня!")
                menu: 
                    "\"Будь по-твоему...\"":
                        label daphne_pre_06_OK:

                        $music("Daphne Privacy")
                        $daphne.SetValue("visitInterval",48)

                        $hermi("~body_50.png// Ну что ж...// То, что ваша любовь - первостатейная стерва я уже говорила.")
                        $hero  ("Мисс, Грейнджер! Она не моя любовь.")
                        $hermi("~body_120.png// Хорошо, пусть будет \"подстилка\".")
                        $hero  ("Она не...")
                        $hermi("Ладно, пока не подстилка. Скоро ею станет.")
                        $hero  ("Мисс! Вы забываетесь! Еще одно слово...")
                        $hermi("~body_103.png// Как будет угодно, сэр. Так вот, эта... особа не имеет друзей, кроме Коровы.")
                        $hero  ("Какой коровы, мисс?")
                        $hermi("~body_186.png// Простите, сэр, это я о Пэнси Паркинсон. Да и ту подругой можно назвать с натяжкой - недостаточно чистокровна для нее.//"
                            "Парня нет. В свободное время бродит по коридорам с задумчивым видом.//"
                            "~body_61.png// Любимые разговоры о чистоте крови - всех уже тошнит от них, даже слизеринцев - не поверите.//"
                            "~body_120.png// На прошлом Осеннем балу ужралась как свинья, простите за грубость сэр, но сравнение весьма точное.//"
                            "Хотя утверждала, что почти не брала в рот.//"
                            "~body_111.png// Что именно она берет в рот, уже простите, не знаю.")
                        $hero  ("Мисс Грейнджер! Вы становитесь несносны! Вы что, ревнуете?")
                        $hermi("~body_66.png// Ревную? К кому, сэр? //~body_186.png// К ЭТОЙ?// Какие глупости... // ~body_193.png// Я просто рассказываю вам, как все обстоит на самом деле, ничего не приукрашивая.")
                        $hermi("~body_83.png// Позволите продолжить?..// Очень любит, когда ее хвалят. Особенно внешность.// ~body_111.png// И это при том, что сиськи можно найти только с лупой...")
                        $hero  ("Гермиона Грейнджер!")
                        $hermi("~body_50.png// Сэр, вы напрасно возмущаетесь, это правда! Я могла наблюдать их в душе, как вас сейчас!")
                        $hero  ("Без лупы нашли, мисс?")
                        $hermi("~body_195.png// Мне очень повезло, сэр, удачно падал свет.//"
                            "~body_100.png// Что еще...// Очень боится уронить свою честь.//"
                            "~body_111.png// Может, где-нибудь уже и уронила, но детали мне неизвестны.")
                        $hero  ("Мисс!")
                        $hermi("~body_100.png// Еще боится своей мамочки, а та боится, что о ней скажут люди - другие чистокровки.//"
                            "Все прочие не люди - их мнением не интересуется.// Семейка не выписывает \"Ежедневный пророк\" - эта газета недостаточно аристократична.//"
                            "Вместо этого читают \"Чистокровные вести\" где пишут о балах, раутах и меряются длиной генеалогического дерева.//"
                            "~body_50.png// Пожалуй, что и все, сэр...//"
                            "~body_103.png// А! Еще ее сова Пухля - обжора еще та, только и ищет, что бы слопать. Не знаю, интересно ли вам это...")
                        $hero  ("Хм... Спасибо, мисс Грейнджер.")
                        $hermi("~body_50.png// Надеюсь, вы получили, что хотели, сэр. А теперь мне пора идти.")
                        $wtevent.Finalize()

                    "\"Так не пойдет!\"":
                        label daphne_pre_06_Cancel:
                        $hermi("~body_206.png// Как угодно. В таком случае, сэр, мой ответ - нет!// Мне нужно идти...")
                        $hermi.liking-=30
            else:
                $hermi("~body_191.png// Даже не надейтесь, что я буду вам помогать, сэр!..// Мне пора!")
                $hermi.liking-=30
    call music_block
    $hermi.Visibility()
    jump hermione_goout



label daphne_pre_finish: #LV.1 (Whoring = 0 - 2)
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Тук-тук-тук!*"
    $daphne.Visibility()
    if IsNextRun(): # Начиная со второго посещения, Дафна в форме чирлидера
        $daphne.ItemSetsCustomize({"body","cheer_start_clothes"},True)
        $daphne.ItemsCustomize(update={"combi:cheer_topbase", "skirt:cheer_long"}).chibi.State(appearance="b")

    menu:
        "\"Кто это?\"":
            $daphne("Это... Это Дафна Гринграсс, сэр. Могу я войти?")
            $hero("Да, входи!")
        "\"Да, входи...\"":
            pass


    
    $music("Daphne Theme")
    $daphne.chibi.State("door", speed="go").Trans(d4, "blink").Trans("go center", "blink") # Если делать dissolve в движении, то сбивается счетчик времени. Лучше выполнить появление чибика стоя, затем уже двигать его 
    pause.5
    $screens.ShowD3("bld1")

    $daphne.State(pos="door").Visibility("body+")("~55 00 1 smi// Добрый день, профессор Дамблдор.") 

    $screens.Show("ctc").Pause().Hide("ctc")


    #$daphne_pre_menu_text=None # текст, который будет говорить джин в конце
#    label daphne_pre_finish_menu:
    if wtevent._finishCount==0: # Первый раз
        $hero  (m, "#(Ну что ж, \"Мисс Голубая Кровь\"... Наша первая встреча и разговоры с Северусом и Гермионой натолкнули меня на пару идей.)") 
        $daphne("~55 00 1 ope// Родители прислали мне сову, что вы будете со мной заниматься.// Чтобы я заняла соответствующую позицию в Хогвартсе.") 
        $hero  (m, "#(Да, дорогая, ты у  меня будешь занимать самые разные позиции.)") 
        $daphne("~55 00 1 pur// Откровенно говоря, я не в восторге от этой идеи...// ...// Сэр?...") 
        $hero  ("Откровенно говоря, я тоже, мисс.") 
        $daphne("~64 w0 1 ope// Что?!... Вы тоже не в восторге?") 
        $hero  ("Хм. Конечно, я мог бы помочь вам, тем более, что я сразу выделил вас из серой массы. У вас есть вкус и стиль.") 
        $daphne("~55 w0 1 smi// Правда, сэр?") 
        $hero  ("Да, мисс. Конечно, я мог бы скрыть от вас этот факт, чтобы вы не возгордились. Но, думаю, вы выше этого.")
        $daphne("~55 w0 1 smi// О, как вы правы, сэр!// Вы... вы сразу проникли в самую глубину!")
        $hero  ("#(Еще не проник, дорогая, но и это не за горами.)")
        $daphne("~46 w0 1 def// Признаюсь, я изначально думала, что вы недостойны учить меня - наследницу древнего рода.") 
        $hero  ("Хм...")
        $daphne("~55 w0 1 smi// Сэр, теперь я понимаю, что, кажется, была неправа.") 
        $hero  ("#(Ты даже не подозреваешь, девочка, насколько!)")
        $daphne("~46 00 1 pou// Профессор Дамблдор! Вот вы сразу заметили, что я особенная девушка!//~37 00 1 pou// А это мугродье, они...") 
        $hero  ("#(Великие пески, только не это! Нужно перевести ее мысли в более подходящее русло.)// Гхм! Мисс, я насчет стиля...// Жаль, конечно, что правилами Хогвартса предписана единая форма верхней одежды.") 
        $daphne("~64 00 1 neu// Да, сэр, это так. Но у меня и правда есть вкус, как у потомственной, чистокровной волшебницы. Такой вкус, что просто ух!//"
            "~64 00 1 def// Будь у меня возможность, я бы им показала, что такое настоящая стильная ведьма!") 
        $hero  ("Но у вас есть такая возможность, мисс.") 
        $daphne("~46 w0 1 smi// Есть?") 
        $hero  ("Вы же - чирлидер, насколько я знаю.// Форма чирлидера в Хогвартсе предполагает некоторую индивидуальность, и вы можете ее показать.// Я готов выступить в роли благодарного зрителя.")
        $daphne("~64 w0 1 ehh// То есть, сэр, вы хотите, чтобы я...") 
        $hero  ("Да-да, Приходили сюда в форме чирлидера. Браво, мисс Гринграсс! Я знал, что вы схватываете быстро, но не думал, что настолько.")
        $daphne("~64 w0 1 dis// Спа-сибо, сэр. Но не кажется ли вам, что несколько странно, если я буду приходить на занятия в этой форме. Она, несколько... эм... вольная.") 
        $hero  ("Мисс Гринграсс, вас ведь не смущает, что вы отплясываете в этой форме перед всем Хогвартсом. Что же такого, если вы придете в ней в кабинет к вашему директору?")
        $daphne("~64 00 1 ope// Но я не уверена...") 
        $hero  ("Возбужде... кxгм!.. возражения не принимаются. Жду вас в следующий раз в форме чирлидера.")

        $daphne("~55 00 1 def// Но вы так и не договорили, сэр, насчет того, почему не в восторге и что могли бы.") 
        $hero  (m, "В следующий раз, мисс. Жду вас через два дня.// А пока у меня есть для вас небольшой подарок.") 
        $daphne("~55 00 1 def// .........") 
        $wtevent.Finalize()

    elif wtevent._finishCount==1: # Второй раз
        $hero  (m, "Замечательно, мисс Гринграсс. Вы выглядите просто сногсшибательно.// При взгляде на вас у любого мужчины поднимется... эм. Настроение..") 
        $daphne("~55 00 1 neu// Вы смущаете меня, профессор. И вряд ли я счастлива от того, что у мужчин что-то там поднимается.//~26 00 1 pou// Я так и знала, что если я приду к вам в этой форме, то все начнется!") 
        $hero  ("Хм. Прошу прощения, что я выразил восторг по поводу вашей внешности, мисс.// Вероятно, вы правы, и мне не стоит отличать вас и делать вам комплименты.")  
        $daphne("~55 n0 1 ehh// Нет, сэр, я не это имела в виду. Просто...// ~55 s0 1 dis// Мне дела нет, если у каких-то грязнокровок что-то там...") 
        $hero  ("\"Поднимается\"? Вы это хотели сказать, мисс?")  
        $daphne("~55 n2 2 ehh// Эм... Ну, да...") 
        $hero  ("Но если это происходит у чистокровных - это ведь совсем другое дело, мисс.")  
        $daphne("~37 n0 2 neu// Сэр, наша беседа идет в каком-то странном направлении!// Если вы не прекратите, я немедленно уйду.") 
        $hero  ("Не прекращу что, мисс?")  
        $daphne("~46 01 2 pou// Обращать на меня ТАКОЕ внимание.") 
        $hero  ("И тем не менее, вы пришли в форме чирлидера.")  
        $daphne("~46 01 2 ope// Но не затем, чтобы вы про меня такое говорили!") 
        $hero  ("#(А зачем же еще, ведьма!)// Конечно, мисс, прошу меня простить.// Обещаю, впредь обращать на вас внимания ровно столько, сколько на любую грязнокровку.")  
        $daphne("~73 00 2 ope// Да нет же, сэр, вы все неправильно понимаете!") 
        $hero  (".......?// Хорошо, мисс, похоже, сегодня не самый удачный день для занятий. Возможно, хороший подарок поднимет вам настроение.")  
        $wtevent.Finalize()

    elif wtevent._finishCount==2: # Третий раз
#        $daphne.ItemsCustomize(delete={"hair"})
#        $daphne.ItemsCustomize(update={"hair"})
        $hero  (m, "Когда вы в этой форме, мисс Гринграсс, я вижу, какое у вас великолепное тело. ")
        $daphne("~55 00 1 pri// Сэр, вы опять!..") 
        $hero  ("Я тут подумал, почему бы вам не выступить в конкурсе мисс Хогвартс?") 
        $daphne("~64 w0 1 ehh// Эмм... Это... это очень неожиданно, сэр. Вы и вправду считаете, что я могла бы?..") 
        $hero  ("Конечно, могли бы. И что, как не победа в конкурсе, вознесет вас на самый верх?")
        $daphne("~64 w0 1 smo// О!..") 
        $hero("У вас отличные шансы. Особенно, если за вас похлопочет директор Хогвартса.")  
        $daphne("~55 00 1 neu// Сэр! Мне это не нужно, я – чистокровная волшебница в Мерлин знает каком поколении.// И я должна получать все просто так, безо всякого там покровительства!") 
        $hero  ("Ну, девочка, не нужно так возмущаться.// Конечно, ты заслуживаешь быть королевой, и я отдал бы тебе первое место прямо сейчас, ни секунды не сомневаясь//"
            "Но ты же понимаешь, сколько вокруг будет худородных, полукровок и откровенного мугродья.// И все они будут тебе завидовать. А МЫ не может допустить, чтобы ты проиграла.")
        $daphne("~64 00 1 neu// Мы?") 
        $hero  ("Мы - волшебники, которые занимают определенное ПОЛОЖЕНИЕ. Такой проигрыш нанесет урон всем НАМ. Ты же понимаешь это?")  
        $daphne("~46 01 1 neu// Хм, я не думала об этом...") 
        $hero  ("А следовало бы, мисс... Если вы готовы преподать урок всем недоволшебникам...")  
        $daphne("~26 n0 1 smo// О, сэр, это мое самое большое желание! Показать им их место. Показать, кто здесь действительно кто. Всем этим девкам...//"
            " ~26 n0 1 wo// Я уже столько лет в Хогвартсе, и что же? Они до сих пор не разглядели, с кем имеют дело!") 
        $hero  ("Отлично, мисс Гринграсс, мне нравится ваш боевой настрой. И я хочу поддержать его небольшим подарком.")  
        $daphne("~55 00 1 def")
        $wtevent.Finalize()

    elif wtevent._finishCount==3: # Четверты и последний раз
        $hero  (m, "Ну что ж, мисс, я заявил вас на конкурс.//"
            "Как раз сейчас списки развешивают по Хогвартсу. А сова с заметкой об этом событии и списком участников уже летит в «Ежедневный пророк».") 
        $daphne("~55 w0 1 ang// О, сэр, все так быстро... я вообще-то не уверена,... я никогда до сих пор...//~55 01 1 dis// Это нужно отменить!") 
        $hero  ("И как это будет выглядеть?//"
            "Вчера вы готовы, а сегодня идете на попятный. Выходит, Дафна Гринграсс спасовала перед грязнокровками?//"
            "Впрочем, если это действительно то, чего вы хотите, я все отменю.")  
        $daphne("~55 01 1 pou// Н-нет, сэр, так нельзя. Но я не знаю, что мне делать...// ~64 00 1 ehh// Вы... вы правда поможете мне?") 
        $hero  ("Конечно, мисс Гринграсс, если вы будете делать то, что я скажу, вам не о чем волноваться.// Вы даже получите удовольствие.")
        $daphne("~64 00 1 dis// Удовольствие, сэр?//"
            "~64 s0 1 dis// Не знаю, какое может быть удовольствие, когда какие-то полукровки оценивают тебя, как племенную сук... эм... корову.") 
        $hero  ("Поверьте мне, мисс, при определенной дрессировке вам понравится быть сук... то есть, коров... то есть стоять на подиуме, да.")  
        $daphne("~26 w0 1 dis// ДРЕССИРОВКЕ, СЭР?!!!")
        $hero(g4, "Кто сказал \"дрессировке\"?")
        $daphne("Вы только что сказали!")
        $hero(m, "О, нет, конечно же, нет, мисс. Я хотел сказать \"тренировке\", да.//"
            "Да и кому может прийти в голову дрессировать такую чистокровную волшебницу, как вы?")
        $daphne("~46 00 1 pou// Вот именно! Если бы кто-то и попытался, он бы сразу понял, что Гринграссы не поддаются дрессировке!")
        $hero("Нет-нет, мисс, у нас будут обычные занятия. Ну, почти обычные, с учетом вашей необыкновенности, конечно.//" 
            "И уверен, в конце вы получите столько удовольствия, сколько еще никогда не получали. #(Хе-хе)")  
        $daphne("~55 00 1 smi// О, вы думаете, когда я займу положение, о котором мы говорили, мне это так понравится?") 
        $hero  (g9, "Даже не сомневайтесь, мисс.")  
        $daphne("~55 00 1 smo// Тогда, сэр, я готова приступить. Чтобы поскорее его занять.") 
        $hero  (m,"Отлично, мисс Гринграсс, и все-таки отдохните сегодня. Я вызову вас, чтобы мы могли приступить к нашим занятим.// И думаю, вы заслуживаете подарка.")  

        $screens.Show(d3, "blktone", "notes")
        $ renpy.play('sounds/win2.mp3') 
        ">Теперь вы можете вызывать Дафну Гринграсс в кабинет."
        $screens.HideD3("blktone")

        $wtevent.Finalize()

    #label daphne_pre_menu(sayText=daphne_pre_menu_text):
    label daphne_pre_menu:
    $item=None
    menu:
        "- Дать ей подарок на прощание -":
            python:
                choose = RunMenu()
                for o in hero.Items():
                    if not o.Name in {"scroll", "ball_dress"}:
                        choose.AddItem("- "+o._caption+" -", "daphne_giving", o.Name)

                choose.Show("daphne_pre_finish_menu")

        "- Ничего -":
            $daphne("Тогда я, наверное, пойду.")



    label daphne_pre_finish_menu:
    $music()
    if item==None:
        $daphne("~55 01 1 pri// #Пообещал подарок, и где он? Скряга...") #Почему-то не срабатывает рот? проверить
        $daphne.liking-=5
    $screens.HideD3("bld1")
    $daphne.Visibility(transition=d3).chibi.Trans("goout door").Hide(d3)    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.5

    #if sayText!=None:
    #    $say(sayText)

#    $hero("...................................")
    call music_block
    return




