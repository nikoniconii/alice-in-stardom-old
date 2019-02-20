################ What type of night is it?

label whatnight:
    
    $ nighttype = renpy.random.randint(1,4)
    
    if nighttype == 1:
        
        jump normalnight
        
    if nighttype == 2:
        
        jump excited
        
    if nighttype == 3:
        
        jump sleepy
        
    if nighttype == 4:
        
        jump insomnia
        
        
        
        
        
        
############ Normal Night

label normalnight:
    
    $ normalnight = renpy.random.randint(1)
    
    if normalnight == 1:
        
        $ day += 1
        
        scene bedalicenight
        with fade
        
        show a smile
        with Dissolve(0.5)
        
        a "{i}After dinner and relaxing at the lounge for a bit, I return to my room to sleep.{/i}"
        a "{i}It has been a long day. It feels good to be back here, resting on the soft bed.{/i}"
        a "{i}I pull the covers up to my shoulders and move into a comfortable position. The sheets smell of fresh lemony detergent, matching the residue of minty mouthwash between my teeth.{/i}"
        a "{i}I close my eyes, ready to be further refreshed by slumber.{/i}"
        
        ###### call screen
        
    if normalnight == 2:
        
        $ day += 1
                
        scene bedalicenight
        with fade
        
        show a smile
        with Dissolve(0.5)
        
        a "{i}Dinner was enjoyable as usual, even after I had to slip past the director and Boss arguing in the hallway afterwards.{/i}"
        a "{i}This place is so huge... I feel like I haven't even began to see all of it!{/i}"
        a "{i}Tomorrow is a new day, and with it, new opportunities.{/i}"
        a "{i}I lay my head down and slowly but surely fall asleep.{/i}"
        
        #### call screen
        
    
    
label excited:
    
    $ excited = renpy.random.randint(1,5)
    
    if excited == 1:
        
        $ day += 1
        
        scene bedalicenight
        with fade
        
        show a smile
        with Dissolve(0.5)
        
        a "{i}So much has happened today.{/i}"
        a "{i}After dinner, I had fun with the others at the lounge. I guess I’m starting to get along after all.{/i}"
        a "{i}It’s amazing, considering that I’ve never even imagined this situation would happen to me. I often still struggle with the idea of being here, but sometimes, I find the courage to face the things coming my way.{/i}"
        a "{i}It’s an opportunity, huh?{/i}"
        a "{i}As much as I usually find Boss to be a vain, money-greedy woman, she does speak some words of wisdom occasionally, doesn’t she?{/i}"
        a "{i}I'll try hard again tomorrow!{/i}"
        a "{i}I tug myself into bed and empty out my thoughts. The unknown future is always scary, but if we were to know everything that would befall us, what fun is life?{/i}"
        a "{i}It’s okay to step into the dark. We’ll find our way eventually.{/i}"
        
        
        ###### call screen
        
    if excited == 2:
        
        $ day += 1
                
        scene bedalicenight
        with fade
        
        show a smile
        with Dissolve(0.5)
        
        a "{i}Phew! Today was a blast!{/i}"
        a "{i}Maybe this whole idol standby thing wasn't such a bad idea after all...{/i}"
        a "{i}I'm going to work extra hard tomorrow, that's for sure!{/i}"
        a "{i}A little rest, and then I'll be back at it tomorrow...{/i}"
        
        ### call screen
        
        
        
label sleepy:
    
    $ sleepy = renpy.random.randint(1,5)
    
    if sleepy == 1:
        
        $ day += 1
                
        scene bedalicenight
        with fade
        
        show a smile
        with Dissolve(0.5)
        
        a "{i}It has been such a hectic day.{/i}"
        a "{i}I almost didn’t want to eat dinner, but knowing I’d be hungry at night otherwise, I stuffed something down my stomach, took a shower, brushed my teeth, then headed off to bed.{/i}"
        a "{i}If not for the soundproof doors and walls, I’m sure I’d still be able to hear sounds of activity outside. The others are probably in the lounge watching a movie or something.{/i}"
        a "{i}I would’ve joined them, but I’m just too tired. My muscles are screaming to be relaxed. I can only comply.{/i}"
        a "{i}I lie down on the bed, relieved that the soft mattress does help my body lose some of its tension.{/i}"
        a "{i}I close my eyes and immediately stop thinking. The darkness envelops me, and before I know it, I fall asleep.{/i}"
        
        ### call screen
        
        
    if sleepy == 2:
        
        $ day += 1
        
        scene bedalicenight
        with fade
        
        show a smile
        with Dissolve(0.5)
        
        a "{i}I never thought anyone could sing so much in one day!{/i}"
        a "{i}After listening to Mary and Taylor practice at the same time for hours on end, I feel like I could just collapse!{/i}"
        a "{i}Between their lovely tones and the soft background music, I'm surprised I wasn't lulled to sleep back there...{/i}"
        a "{i}But, my bed looks so comfy... Just a little rest before tomorrow will be good.{/i}"
        
        
        ###### call screen
        
        
        
        
label insomnia:
    
    $ insomnia = renpy.random.randint(1,5)
    
    if insomnia == 1:
        
        $ day += 1
                
        scene bedalicenight
        with fade
        
        show a smile
        with Dissolve(0.5)
        
        a "{i}It has been a long day.{/i}"
        a "{i}After dinner, I took a shower, brushed my teeth, and headed off to bed, but somehow, I couldn’t sleep.{/i}"
        a "{i}I drag myself up to a sitting position and just stay like that, hunched over my bed for a moment. Should I turn on the lights and read for a bit?{/i}"
        a "{i}I haven’t finished the paperback I’ve been reading on my commutes before coming here, but if I start now, I doubt I could stop. Maybe I should do something less engaging.{/i}"
        a "{i}I decide to take a walk. The night outside looks lovely.{/i}"
        
        scene fountainnight
        with fade
        
        show a smile
        with Dissolve(0.5)
        
        a "{i}I take the elevator to the roof where a garden stands. At this hour, it’s quite dark, but parts of the garden remain lighted with panels of LED lights. The fountain looks stunning with colors playing on the rippling water surface.{/i}"
        a "{i}I sit down on the stone by the fountain, hearing the water rise and fall. Looking upwards, I can faintly make out the stars above me.{/i}"
        a "{i}It’s too bright here in the city to see star curtains, but the few twinkling in the dark, heavenly seas still look beautiful as rare gems.{/i}"
        a "{i}It’s weird that I prefer this view over the view overlooking the rest of the city. We’re easily on the tallest building in town, but there is something more enticing about nature, especially at a time like this.{/i}"
        a "{i}While looking down at all the houses and streets below may give a feeling of power and entitlement, looking at the endless expanse above is far more liberating.{/i}"
        a "{i}I breathe in a breath of fresh air. It’s a little cold here by night, but the crisp, clean feeling is nonetheless amazing. It makes my worries slip away one by one.{/i}"
        a "{i}Alright, I can do this.{/i}"
        a "{i}I need not care about how others view me. I need not care about the outcome of this challenge. I just need to try as hard as I can.{/i}"
        a "{i}I’d be able to live up to myself then.{/i}"
        
        scene bedalicenight
        with fade
        
        a "{i}Empowered with renewed confidence, I snuggle back into bed. I may like the rooftop garden, but there’s nothing better than a warm bed on a cold night.{/i}"
        a "{i}With the weight of all my pressures finally lifting away, I drift off into sleep.{/i}"
        
        
        ##### call  screen
        
        
        
        
        
        
        
        
        
        
        
        
        
        


