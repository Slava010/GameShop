
isLogin = False
isAdmin = False

category = 'All'
user = None

categoryes = [
    'All',
    'Andventure',
    'Raicing',
    'Horror'
]

users = [
    {
        'login': 'user',
        'password': '1111',
        'img': 'https://avatars.akamai.steamstatic.com/734554f997eec3a0b54aed2f4725df84def647f8_full.jpg',
        'isAdmin': False
    },
    {
        'login': 'admin',
        'password': '2222',
        'img': 'https://klike.net/uploads/posts/2019-11/1573725816_14.jpg',
        'isAdmin': True
    }
]

products = [
    {
        'name': 'God of War',
        'img': 'https://upload.wikimedia.org/wikipedia/ru/thumb/5/5a/God_of_War_2018_cover.jpg/274px-God_of_War_2018_cover.jpg',
        'price': 59.99,
        'comments': [
            {
                'user': users[0],
                'raiting': 10,
                'comment': 'GOTY!!',
            }
        ],
        'screens': [
            'https://itc.ua/wp-content/uploads/2022/08/gowr11.jpg',
            'https://images.pushsquare.com/screenshots/82983/large.jpg',
            'https://cdn.akamai.steamstatic.com/steam/apps/1593500/ss_93a3ca63aa2cd8c675bbb6430324ee3f2d44b845.1920x1080.jpg?t=1650554420',
        ],
        'category': 'Andventure'
    },
    {
        'name': 'Red Dead Redemption 2',
        'img': 'https://lh3.googleusercontent.com/HCUkD69MAHEOj84Yi7Kb5vxHpCePTsmQI4g9vYuVPUo-87cWE6ZZIk0tiyYzaiS9zaAFMTXRNYJaaRczRN-yQYw',
        'price': 59.99,
        'comments': [
            {
                'user': users[0],
                'raiting': 10,
                'comment': 'The best game ever!',
            }
        ],
        'screens':[
            'https://img.redbull.com/images/c_crop,w_2897,h_1449,x_0,y_0,f_auto,q_auto/c_scale,w_1200/redbullcom/2019/01/21/c3f2f474-cc17-45df-883d-6008da02d792/red-dead-redemption-2-mysteries',
            'https://i.blogs.es/448439/red-dead-redemption-2-mod/1366_2000.png',
            'https://www.cnet.com/a/img/resize/074b14ef40267c1c4f1070ddd3c86fe8ef35829b/hub/2018/10/25/776b9111-60ec-4e79-9f16-8372eac0635c/red-dead-redemption-2-20181021172719.jpg?auto=webp&width=768',
        ],
        'category': 'Andventure'
    },
    {
        'name': 'Burnout Paradise',
        'img': 'https://upload.wikimedia.org/wikipedia/ru/c/c7/Burnout_Paradise_Coverart.jpg',
        'price': 9.99,
        'comments': [
            {
                'user': users[0],
                'raiting': 8,
                'comment': 'Good!',
            }
        ],
        'screens':[
            'https://itc.ua/wp-content/uploads/2018/02/BOPR_Screenshot_4k_04_RearMuscle.jpg',
            'https://i0.wp.com/spillhistorie.no/wp-content/uploads/2018/02/Burnout-Paradise-Remastered.jpg?fit=800%2C400&ssl=1',
            'https://ocs-pl.oktawave.com/v1/AUTH_2887234e-384a-4873-8bc5-405211db13a2/spidersweb/2020/07/burnout-paradise-remastered-8-1000x563.jpg',
        ],
        'category': 'Raicing'
    },
    {
        'name': 'need for speed 2015',
        'img': 'https://upload.wikimedia.org/wikipedia/ru/0/08/Need_for_Speed_Coverart.jpg',
        'price': float(4.99),
        'comments': [
            {
                'user': users[0],
                'raiting': 8,
                'comment': 'Interesting!',
            }
        ],
        'screens':[
            'https://i.playground.ru//i/screenshot/75747/need_for_speed.jpg',
            'https://i.playground.ru//i/screenshot/75742/need_for_speed.jpg',
            'https://vgtimes.ru/uploads/gallery/main/137264/nfs_pc_reveal_03.jpg',
        ],
        'category': 'Raicing'
    },
    {
        'name': "Resident Evil 8",
        'img': 'https://upload.wikimedia.org/wikipedia/ru/2/24/%D0%9E%D0%B1%D0%BB%D0%BE%D0%B6%D0%BA%D0%B0_Resident_Evil_Village.jpg',
        'price': float(49.99),
        'comments': [
            {
                'user': users[0],
                'raiting': 9,
                'comment': 'The besr RE!',
            }
        ],
        'screens':[
            'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/0276f574-98ea-4e2d-ba44-68f500bf01bc/ddzwpfm-4e81e118-5d93-4b0e-9a00-606c145cad24.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzAyNzZmNTc0LTk4ZWEtNGUyZC1iYTQ0LTY4ZjUwMGJmMDFiY1wvZGR6d3BmbS00ZTgxZTExOC01ZDkzLTRiMGUtOWEwMC02MDZjMTQ1Y2FkMjQuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.KlqtvcmYFkkY7AzrZiYDXXGIqdN6iHdkh0nOOx372XU',
            'https://images7.alphacoders.com/108/1081776.jpg',
            'https://sm.ign.com/t/ign_nordic/gallery/r/resident-e/resident-evil-8-village-showcase-screenshots_b4wt.1080.jpg',
        ],
        'category': 'Horror'
    },
    {
        'name': "The Evil Within",
        'img': 'https://upload.wikimedia.org/wikipedia/ru/4/4e/The_Evil_Within_Cover_Art.jpeg',
        'price': float(4.99),
        'comments': [
            {
                'user': users[0],
                'raiting': 5,
                'comment': 'Good game , but worst perfomance :(',
            }
        ],
        'screens':[
            'https://www.trueachievements.com/customimages/024870.jpg',
            'https://ip.trueachievements.com/remote/dlassets-ssl.xboxlive.com/public/content/3f5cd5d9-a950-4acb-a752-86eafb3cccc4/09e0ee6a-3868-44b0-88fb-9fbe8ab59fbb/4c9ebe15-a742-47cc-a5aa-ac4be0e83718.png?width=900',
            'https://www.newgamenetwork.com/images/uploads/gallery/EvilWithin/tew_09.jpg',
        ],
        'category': 'Horror'
    },
    {
        'name': "Cyberpunk 2077",
        'img': 'https://upload.wikimedia.org/wikipedia/ru/b/bb/%D0%9E%D0%B1%D0%BB%D0%BE%D0%B6%D0%BA%D0%B0_%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BD%D0%BE%D0%B9_%D0%B8%D0%B3%D1%80%D1%8B_Cyberpunk_2077.jpg',
        'price': float(49.99),
        'comments': [
            {
                'user': users[0],
                'raiting': 6,
                'comment': 'So many bugs in this perfect game :(',
            }
        ],
        'screens':[
            'https://cdn.wccftech.com/wp-content/uploads/2020/06/Cyberpunk-2077-Jun-25th-Screenshots-9.jpg',
            'https://gamespot.com/a/uploads/original/225/2256286/3428196-dlimunjx4aejnwc.jpg',
            'https://www.gamersyde.com/newsv3/new_cyberpunk_2077_screenshots-21697.jpg',
        ],
        'category': 'Adventure'
    },
    {
        'name': "Witcher 3: Wild Hunt",
        'img': 'https://image.api.playstation.com/vulcan/ap/rnd/202211/0712/Ksx2eULkKzp7sXAuAJcnmSGn.png',
        'price': float(29.99),
        'comments': [
            {
                'user': users[0],
                'raiting': 10,
                'comment': 'Dandelion, damn it!',
            }
        ],
        'screens':[
            'https://staticg.sportskeeda.com/wp-content/uploads/2015/03/1371178393-some-creatures-will-be-more-prone-to-inflammation-than-others-the-igni-singn-works-perfectly-on-the-fiend-1426877938.jpg',
            'https://gamingbolt.com/wp-content/uploads/2015/03/The-Witcher-3.jpeg',
            'https://c4.wallpaperflare.com/wallpaper/707/315/666/the-witcher-3-wild-hunt-geralt-of-rivia-landscape-video-games-wallpaper-preview.jpg',
        ],
        'category': 'Adventure'
    },
    {
        'name': "Amnesia: The Dark Descent",
        'img': 'https://upload.wikimedia.org/wikipedia/en/6/62/Amnesia-The-Dark-Descent-Cover-Art.png',
        'price': float(4.99),
        'comments': [
            {
                'user': users[0],
                'raiting': 10,
                'comment': 'Perfect!',
            }
        ],
        'screens':[
            'https://www.newgamenetwork.com/images/uploads/gallery/Amnesia/Amnesia%202010-09-11%2018-29-06-38.jpg',
            'https://bloody-disgusting.com/wp-content/uploads/2018/10/amnesia-header.jpg',
            'https://c4.wallpaperflare.com/wallpaper/707/315/666/the-witcher-3-wild-hunt-geralt-of-rivia-landscape-video-games-wallpaper-preview.jpg',
        ],
        'category': 'Horror'
    },
]

def GetProductByName(name: str):
    for product in products:
        if(product['name'] == name):
            return product
    return None
