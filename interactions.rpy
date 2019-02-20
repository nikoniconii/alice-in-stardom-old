###########################################################################################################
########################################### INTERACTIONS ##################################################
###########################################################################################################

######## PLACE LIST ########

# Mary's Room
# Taylor's Room
# Cherry's Room
# Music Hall
# Lounge
# Shopping Area


label entrancehall:
    
    $ int1 = renpy.random.randint(1,5)
    
    if int1 == 1:
        
        scene hallday
        
        a "{i}I need to relax for a bit. Let's spend the time taking a walk outside our residential complex.{/i}"
        
        
        

label aliceroom:
    
    $ int2 = renpy.random.randint(1,5)
    
    if int2 == 1:
        
        scene bedaliceday
        
        a "{i}I am a little tired. I need to take a nap.{/i}"
        
        
        
        
label maryroom:
    
    $ int3 = renpy.random.randint(1,5)
    
    if mary >= 8:
        
        scene hallday
        with fade
        
        show a frown
        with Dissolve(0.5)
        
        a "{i}The stress is really eating me away. I feel sick.{/i}"
        a "{i}It’s weird, because I keep trying to convince myself that I have nothing to lose. I should stop caring so much. After all, Boss got the backup contestant she wanted.{/i}"
        a "{i}Even if I were to get eliminated, I would’ve fulfilled the purpose. It’s not as though I would be punished or anything.{/i}"
        a "{i}Life will go on as it always has. I get to keep my job. I get to keep the old roof atop my head. All is good, right? This month will just be a little vacation - and it’s for free too! Like what else could I have hoped for?{/i}"
        a "{i}But saying all this isn’t making my heart feel any easier. I don’t want to give myself any false hopes, but it just keeps coming to me either way.{/i}"
        a "{i}Truth is, I do want to win, huh? Even if it were impossible.{/i}"
        a "{i}The contradiction leaves me in my current state. I’m just too preoccupied with these thoughts to focus on training.{/i}"
        a "{i}And yet, who can I talk to about all this? My mom? She’d just say I’m silly. It’s not that she really wants to chide me, but she’d think that putting it lightly would make me feel better.{/i}"
        a "{i}Guess where I inherited these genes of idiocy from? They obviously have to come from somewhere...{/i}"
        a "{i}Sorry, Mom.{/i}"
        a "{i}So I end up just wandering around the mansion, trying to keep my mind off things. I mean, just look at everything here, so ridiculously lavish.{/i}"
        a "{i}I’m sure some exotic vase from some distant Chinese dynasty or whatnot would be enough to keep me preoccupied... maybe...{/i}"
        a "{i}Before I know it, I’m here, in front of Mary’s room. The door is left open.{/i}"
        a "{i}Why am I even here? I mean, I’ve been hanging out with Mary a little, but that doesn’t mean I intend to confide my problems with her!{/i}"
        a "{i}I was about to walk away when something within her room captures my gaze. It’s a painting. Mary is busily working on it - probably the reason why she has yet to notice my presence.{/i}"
        a "{i}The painting is not clean and neat. I can’t exactly pinpoint what she is painting at all. But the turbulent colors resonate with my heart.{/i}"
        a "{i}Blazing hues evoke pride and confidence, lighter yellows speak of a more subdued hope. Then all of this mingles and clashes, forming darker streaks at their interface, just like the doubts I am feeling.{/i}"
        
        m "Alice...?"
        
        show a shock at right
        show m blush at left
        with Dissolve(0.5)
        
        a "Ah! I'm sorry! I didn't mean to peak!"
        
        a "{i}Well, I already did. Like my denial amounts to anything.{/i}"
        
        show m talk at left
        
        m "I don't mind an audience."
        
        show m smile at left
        show a cute at right
        
        a "I see..."
        
        show m talk at left
        
        m "It means that you can come in and take a seat if you want."
        
        show m smile at left
        
        a "Thanks."
        
        a "{i}It’d be rude if I refused. Plus, I do actually want to take a closer look at the painting.{/i}"
        
        scene bedmaryday
        with fade
        
        show a blush at right
        show m smile at leftt
        with Dissolve(0.5)
        
        a "You're so good at everything you do, Mary."
        
        a "{i}I can’t help but utter this sentence. It may sound like a praise to Mary, but maybe I’m just saying it to myself to reaffirm my own incompetence.{/i}"
        
        show m talk at leftt
        
        m "This is just a random splatter of paint. I’m sure anybody can do it."
        
        show m smile at leftt
        
        a "You've got to be kidding."
        
        show m talk at leftt
        
        m "Why would I be? Do you see anything distinct here?"
        
        show m smile at leftt
        
        a "Well... no..."
        
        show m talk at leftt
        
        m "That’s because I’m not an artist. I merely enjoy the feel of putting paint on canvas."
        
        show m smile at leftt
        
        a "But... it looks good."
        
        show m talk at leftt
        
        m "The paint is good quality, I suppose."
        
        show m smile at leftt
        
        a "{i}I don’t know what to say. Mary does sound serious here. So she hasn’t ever had any formal artistic training?{/i}"
        
        a "You must be really talented then."
        
        show m talk at leftt
        
        m "Or I just have the guts to waste high quality paint on high quality canvas? What makes you think you can’t do the same?"
        
        show m smile at leftt
        
        a "I didn’t get very high grades whenever painting is concerned."
        
        show m talk at leftt
        
        m "I didn’t get any grades on painting because I never took a class. Now kill me."
        
        show m smile at leftt
        
        a "{i}I enjoy a little laugh with Mary. She then hands her brush over to me.{/i}"
        
        show m talk at leftt
        
        m "Here, give it a try."
        
        show m smile at leftt
        
        a "You mean... on your painting?"
        
        show m talk at leftt
        
        m "Why not? It’s not as though I’m trying to sell it. And who knows, maybe after your expert fine-tuning, it’d really be worthy of sale."
        
        show m smile at leftt
        
        a "{i}I reluctantly take up the brush and wonder how should I start. What color should I use? Where should I paint?{/i}"
        a "{i}Mary’s painting is already perfect without my tampering, perfect just like her.{/i}"
        
        show m talk at leftt
        show a cute at right
        
        m "Why are you hesitating?"
        
        show m smile at leftt
        
        a "I... I don't want to make it worse."
        
        show m talk at leftt
        
        m "What do you mean worse?"
        
        show m smile at leftt
        
        a "I... don't really know. If I knew, I wouldn't mess it up, right?"
        
        a "{i}Mary sighs, coming around behind me. She clasps onto my hand that is holding the brush.{/i}"
        
        show m talk at leftt
        
        m "Now paint. If I don’t like what you do, I’d be able to stop you. I bear the final responsibility here."
        
        show m smile at leftt
        
        a "Mary?"
        
        show m talk at leftt
        
        m "Look, Alice. You need to be more confident."
        
        show m smile at leftt
        
        a "I know. I'm trying."
        
        show m talk at leftt
        
        m "But you think the problem of your wavering is that you’re not good enough to be confident?"
        
        show m smile at leftt
        
        a "How did you..."
        
        show m talk at leftt
        
        m "It's all over your face. At the show, while you're practising here, heck, while you are walking these halls - you just give off the aura of \"I'm not good enough\"."
        
        show m smile at leftt
        
        a "But I'm {i}not{/i} good enough. I'm not like you."
        
        show m talk at leftt
        
        m "Not as rich as me? Being rich doesn’t make you a better singer."
        
        show m smile at leftt
        
        a "But you were born in this kind of environment. You know how to act in this kind of environment."
        
        show m talk at leftt
        
        m "Which is what? To act like what common people like you would call snobs? I am well-aware of what people call me behind my back."
        
        show m smile at leftt
        show a shock at right
        
        a "That's... I don't mean to put it that way..."
        
        show m talk at leftt
        
        m "And I do not take offense. People react differently to the environment around them. There is no right or wrong. Why can’t you gawk at the beautiful furnishings and call it a waste of societal resources like Taylor does?"
        
        show m frown at leftt
        
        a "I suppose I can…but that’s not the issue here, right? The rich thing... yes. I guess I have felt a little inferior because of it and come to think of it, it is stupid. But rich or not, you and the others are better singers. I can’t change that!"
        
        m "Yes you can. If you work harder. If you pour your heart into it."
        
        a "I don't believe I...{w=1.0}{nw}"
        
        show m talk at leftt
        
        m "Then believe."
        
        show m smile at leftt
        
        a "{i}Mary plunges the brush into pure red paint and presses it against the canvas.{/i}"
        
        a "No!"
        
        show m talk at leftt
        
        m "It's not too late to change what I'm doing. Fight me for control over the brush."
        
        show m smile at leftt
        
        a "{i}I finally strengthen my grip and drag the brush in a curve down the left side of the painting, then with the remainder of the paint, I draw a similar curve down the right side.{/i}"
        a "{i}It’s a heart, my heart, bleeding red.{/i}"
        
        a "These are my feelings. I want to have hope, but whenever I feel it, it’s accompanied by darkness. I’m worried that I won’t succeed. It’s stupid, because I have no right to be asking for success to begin with!"
        
        show m talk at leftt
        
        m "You have every right."
        m "Didn’t I draw this because it’s exactly what I felt, too?"
        m "You may think that I’m confident and proud, but like you said, whenever you have hope, you’d have the worry of not fulfilling the hope. It’s like wherever there is light, a shadow would be cast."
        
        show m smile at leftt
        show a shock at right
        
        a "{i}I can’t quite believe Mary would have such mundane worries too. She should have no doubts that she’d at least be a finalist!{/i}"
        
        show m talk at leftt
        
        m "I think the heart you painted really completes the picture. It shows that anybody with a heart can be bothered by these conflicting emotions."
        m "It may be so painful that it’s like our hearts are bleeding! But look, isn’t the red so vivid? This must be what it means to be alive."
        
        show m smile at leftt
        show a blush at right
        
        a "You make everything sound so sentimental, Mary..."
        
        show m talk at leftt
        
        m "You’re the one who painted it."
        
        show m smile at leftt
        
        a "Didn’t you say you were gonna bear the final responsibility?"
        
        a "{i}We laugh together again. Mary pats my shoulder, smiling.{/i}"
        
        show m talk at leftt
        
        m "Look, Alice. We’re all on the same boat. Don’t doubt yourself. All of us should have the right to want to win. That’s why we are here."
        
        show m smile at leftt
        show a cute at right
        
        a "{i}I don’t know what to say. Maybe Mary is right. Even if I don’t stand a chance of winning, I can still dream, right?{/i}"
        
        a "Thanks. I think I feel better now."
        
        show m talk at leftt
        
        m "Knowing that you aren’t the only one who thinks badly of yourself?"
        
        show m smile at leftt
        
        a "Well... it came as a surprise that you’d also have these thoughts... and I hate to admit it, but yeah, I guess I do feel better knowing I’m not alone."
        
        show m frown at right
        
        m "Asshole."
        
        show m talk at right
        
        m "But I feel better too. I don’t like being alone either."
        
           
        
    if mary <= 8:    
    
        if int3 == 1:
            
            scene bedmaryday
            
            a "{i}I wanted to ask Mary for some advice, but it seems like she's not in her room. Maybe next time.{/i}"
        
        
        
label taylorroom:
    
    $ int4 = renpy.random.randint(1,5)
    
    if int4 == 1:
        
        scene bedtaylorday
        
        a "{i}I wanted to ask Taylor for some words of confidence, but it seems like he isn't in his room. Maybe another time.{/i}"
        
        
        
label lisroom:
    
    $ int5 = renpy.random.randint(1,5)
    
    if int5 == 1:
        
        scene bedlisday
        
        a "{i}I wanted to ask Lis for some advice, but seems like she's not in her room. Maybe another time.{/i}"
        
        

label cherryroom:
    
    $ int6 = renpy.random.randint(1,5)
    
    if int6 == 1:
        
        scene bedcherryday
        
        a "{i}I wanted to ask Cherry for some advice, but it seems like she is not in her room. Maybe next time.{/i}"
        
        
        
label grantroom:
    
    $ int7 = renpy.random.randint(1,5)
    
    if int7 == 1:
        
        scene bedgrantday
        
        a "{i}I wanted to ask Grant for a few words of advice, but he's not in his room. Maybe another time.{/i}"
        

label katjaroom:
    
    $ int8 = renpy.random.randint(1,5)
    
    if int8 == 1:
        
        scene penthouseday
        
        a "{i}I wanted to speak with Boss, but she's not in her penthouse. Maybe next time.{/i}"
        
        

label stage:
    
    $ int9 = renpy.random.randint(1,5)
    
    if int9 == 1:
        
        scene stageclose
        
        a "{i}I wanted to speak with the director, but seems like he is away at the moment. Maybe next time.{/i}"
        
        
        
label musicroom:
    
    $ int11 = renpy.random.randint(1,5)
    
    if int11 == 1:
        
        scene musicroom
        with fade
        
        a "{i}Seems like I'm the only one in the music room. Let's use the opportunity to practice lots!{/i}"
        
    if int11 == 2:
        
        scene musicroom
        with fade
        
        a "{i}I should really get some practicing done. I'm still not very confident about my skills.{/i}"
        a "{i}I head down to the music room. Seems like Mary is already there.{/i}"
        
        show a smile at right
        show m smile at left
        with Dissolve(0.5)
        
        show m talk at left
        
        m "You here to practice too?"
        
        show m smile at left
        
        a "Yeah, I was thinking about it, but if you want to be left alone..."
        
        show m talk at left
        
        m "Let's practice together."
        
        show m smile at left
        show a cute at right
        
        a "You sure? I'm not really good, and..."
        
        show m talk at left
        
        m "Do you have a secret skill you're hiding or something?"
        
        show m smile at left
        show a blush at right
        
        a "Of course not!"
        
        show m talk at left
        
        m "Then why hesitate? Let's work together to become better singers."
        
        show m smile at left
        
        a "{i}If Mary is willing to practise with me, I think I’d benefit a lot from working with her. It’d be more fun to have company too. Mary is actually quite nice now that I’m getting to know her better.{/i}"
        
        a "Alright. Let's start!"
        
        $ mary += 1
        
        
        
label diningroom:
    
    $ int12 = renpy.random.randint(1,5)
    
    if int12 == 1:
        
        scene dinningday
        
        a "{i}Nobody is around, but I can still enjoy a snack myself, right? Or can I try my hands at cooking something. I'm sure it would be a nice way to relax!{/i}"
        
        
label lounge:
    
    $ int13 = renpy.random.randint(1,5)
    
    if int13 == 1:
        
        scene loungeday
        
        a "{i}I haven't watched TV in a while. Gotta catch up on some sappy romance drama and watch the news!{/i}"
        
        
label workout:
    
    $ int14 = renpy.random.randint(1,5)
    
    if int14 == 1:
        
        scene workoutday
        
        a "{i}Seems like I'm the only one in the workout room today. Well, I'll just have a quiet workout by myself. How nice!{/i}"
        
        
label rooftop:  ## garden
    
    $ int15 = renpy.random.randint(1,5)
    
    if int15 == 1:
        
        scene fountainday
        with fade
        
        a "{i}I really need a breath of fresh air. I enjoy the peace and serenity of the rooftop garden.{/i}"
        
    if int15 == 2:
        
        scene fountainday
        with fade
        
        a "{i}I really need a breath of fresh air. I head upstairs to the rooftop garden.{/i}"        
        a "{i}Seems like I’m not the only one. Mary is also at the garden, practicing.{/i}"
        
        show a smile at right
        show m smile at left
        with Dissolve(0.5)
        
        a "Hey, Mary."
        
        show m talk at left
        
        m "Good morning. Are you here to practice too?"
        
        show m smile at left
        show a sing at right
        
        a "Nah. I'm just here to relax."
        
        show m talk at left
        show a smile at right
        
        m "I'm not disturbing you, right? I can practice elsewhere if you want."
        
        show m smile at left
        
        a "That's okay. You aren't bothering me."
        
        show m talk at left
        
        m "Thanks."
        
        show m smile at left
        
        a "{i}Mary continues practicing, projecting her voice into the crisp, morning air. I have fun watching her, even learning a bit along the way.{/i}"
        
        $ mary += 1
        
        
        
label shopping:
    
    $ int16 = renpy.random.randint(1,5)
    
    if int16 == 1:
        
        scene shop
        
        a "{i}I need a break from everything. I have fun doing some shopping on my own.{/i}"
















































