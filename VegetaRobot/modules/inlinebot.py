        elif text.split()[0] == "pokedex":
            if len(text.split()) < 2:
                await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Pokemon [text]",
                    switch_pm_parameter="pokedex",
                )
                return
            pokedex = text.split(None, 1)[1].strip()
            Pokedex = await pokedexinfo(answers, pokedex)
            await client.answer_inline_query(query.id, results=Pokedex, cache_time=2)
        elif text.split()[0] == "paste":
            tex = text.split(None, 1)[1]
            answerss = await paste_func(answers, tex)
            await client.answer_inline_query(query.id, results=answerss, cache_time=2)

        elif text.split()[0] == "covid":
            lel = text.split(None, 1)[1]
            results = []
            country = lel.replace(" ", "")
            data = await fetch(f"https://corona.lmao.ninja/v2/countries/{country}")
            data = await json_prettify(data)
            results.append(
                InlineQueryResultArticle(
                    title="Covid Info Gathered succesfully",
                    description=data,
                    input_message_content=InputTextMessageContent(
                        data, disable_web_page_preview=False
                    ),
                )
            )
            await client.answer_inline_query(query.id, results=results, cache_time=2)
        elif text.split()[0] == "country":
            lel = text.split(None, 1)[1]
            results = []
            country = CountryInfo(lel)
            try:
                a = country.info()
            except:
                a = "Country Not Avaiable Currently"
            name = a.get("name")
            bb = a.get("altSpellings")
            hu = ""
            for p in bb:
                hu += p + ",  "

            area = a.get("area")
            borders = ""
            hell = a.get("borders")
            for fk in hell:
                borders += fk + ",  "

            call = ""
            WhAt = a.get("callingCodes")
            for what in WhAt:
                call += what + "  "

            capital = a.get("capital")
            currencies = ""
            fker = a.get("currencies")
            for FKer in fker:
                currencies += FKer + ",  "

            HmM = a.get("demonym")
            geo = a.get("geoJSON")
            pablo = geo.get("features")
            Pablo = pablo[0]
            PAblo = Pablo.get("geometry")
            EsCoBaR = PAblo.get("type")
            iso = ""
            iSo = a.get("ISO")
            for hitler in iSo:
                po = iSo.get(hitler)
                iso += po + ",  "
            fla = iSo.get("alpha2")
            fla.upper()

            languages = a.get("languages")
            lMAO = ""
            for lmao in languages:
                lMAO += lmao + ",  "

            nonive = a.get("nativeName")
            waste = a.get("population")
            reg = a.get("region")
            sub = a.get("subregion")
            tik = a.get("timezones")
            tom = ""
            for jerry in tik:
                tom += jerry + ",   "

            GOT = a.get("tld")
            lanester = ""
            for targaryen in GOT:
                lanester += targaryen + ",   "

            wiki = a.get("wiki")

            caption = f"""<b><u>Information Gathered Successfully</b></u>
                <b>
                Country Name:- {name}
                Alternative Spellings:- {hu}
                Country Area:- {area} square kilometers
                Borders:- {borders}
                Calling Codes:- {call}
                Country's Capital:- {capital}
                Country's currency:- {currencies}
                Demonym:- {HmM}
                Country Type:- {EsCoBaR}
                ISO Names:- {iso}
                Languages:- {lMAO}
                Native Name:- {nonive}
                population:- {waste}
                Region:- {reg}
                Sub Region:- {sub}
                Time Zones:- {tom}
                Top Level Domain:- {lanester}
                wikipedia:- {wiki}</b>
                Gathered By @ZeusXRobot.</b>
                """
            results.append(
                InlineQueryResultArticle(
                    title=f"Infomation of {name}",
                    description=f"""
                Country Name:- {name}
                Alternative Spellings:- {hu}
                Country Area:- {area} square kilometers
                Borders:- {borders}
                Calling Codes:- {call}
                Country's Capital:- {capital}
        
                Touch for more info
                """,
                    input_message_content=InputTextMessageContent(
                        caption, parse_mode="HTML", disable_web_page_preview=True
                    ),
                )
            )
            await client.answer_inline_query(query.id, results=results, cache_time=2)

        elif text.split()[0] == "fakegen":
            results = []
            fake = Faker()
            name = str(fake.name())
            fake.add_provider(internet)
            address = str(fake.address())
            ip = fake.ipv4_private()
            cc = fake.credit_card_full()
            email = fake.ascii_free_email()
            job = fake.job()
            android = fake.android_platform_token()
            pc = fake.chrome()
            res = f"<b><u> Fake Information Generated</b></u>\n<b>Name :-</b><code>{name}</code>\n\n<b>Address:-</b><code>{address}</code>\n\n<b>IP ADDRESS:-</b><code>{ip}</code>\n\n<b>credit card:-</b><code>{cc}</code>\n\n<b>Email Id:-</b><code>{email}</code>\n\n<b>Job:-</b><code>{job}</code>\n\n<b>android user agent:-</b><code>{android}</code>\n\n<b>Pc user agent:-</b><code>{pc}</code>"
            results.append(
                InlineQueryResultArticle(
                    title="Fake infomation gathered",
                    description="Click here to see them",
                    input_message_content=InputTextMessageContent(
                        res, parse_mode="HTML", disable_web_page_preview=True
                    ),
                )
            )
            await client.answer_inline_query(query.id, cache_time=0, results=results)

        elif text.split()[0] == "cs":
            results = []
            score_page = "http://static.cricinfo.com/rss/livescores.xml"
            page = urllib.request.urlopen(score_page)
            soup = BeautifulSoup(page, "html.parser")
            result = soup.find_all("description")
            Sed = ""
            for match in result:
                Sed += match.get_text() + "\n\n"
            res = f"<b><u>Match information gathered successful</b></u>\n\n\n<code>{Sed}</code>"
            results.append(
                InlineQueryResultArticle(
                    title="Match information gathered",
                    description="Click here to see them",
                    input_message_content=InputTextMessageContent(
                        res, parse_mode="HTML", disable_web_page_preview=False
                    ),
                )
            )
            await client.answer_inline_query(query.id, cache_time=0, results=results)

        elif text.split()[0] == "antonyms":
            results = []
            lel = text.split(None, 1)[1]
            word = f"{lel}"
            let = dictionary.antonym(word)
            set = str(let)
            jet = set.replace("{", "")
            net = jet.replace("}", "")
            got = net.replace("'", "")
            results.append(
                InlineQueryResultArticle(
                    title=f"antonyms for {lel}",
                    description=got,
                    input_message_content=InputTextMessageContent(
                        got, disable_web_page_preview=False
                    ),
                )
            )
            await client.answer_inline_query(query.id, cache_time=0, results=results)

        elif text.split()[0] == "synonyms":
            results = []
            lel = text.split(None, 1)[1]
            word = f"{lel}"
            let = dictionary.synonym(word)
            set = str(let)
            jet = set.replace("{", "")
            net = jet.replace("}", "")
            got = net.replace("'", "")
            results.append(
                InlineQueryResultArticle(
                    title=f"antonyms for {lel}",
                    description=got,
                    input_message_content=InputTextMessageContent(
                        got, disable_web_page_preview=False
                    ),
                )
            )
            await client.answer_inline_query(query.id, cache_time=0, results=results)

        elif text.split()[0] == "define":
            results = []
            lel = text.split(None, 1)[1]
            word = f"{lel}"
            let = dictionary.meaning(word)
            set = str(let)
            jet = set.replace("{", "")
            net = jet.replace("}", "")
            got = net.replace("'", "")
            results.append(
                InlineQueryResultArticle(
                    title=f"Definition for {lel}",
                    description=got,
                    input_message_content=InputTextMessageContent(
                        got, disable_web_page_preview=False
                    ),
                )
            )
            await client.answer_inline_query(query.id, cache_time=0, results=results)

        elif text.split()[0] == "weather":
            results = []
            sample_url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"
            input_str = text.split(None, 1)[1]
            async with aiohttp.ClientSession() as session:
                response_api_zero = await session.get(
                    sample_url.format(input_str, OPENWEATHERMAP_ID)
                )
            response_api = await response_api_zero.json()
            if response_api["cod"] == 200:
                country_code = response_api["sys"]["country"]
                country_time_zone = int(response_api["timezone"])
                sun_rise_time = int(response_api["sys"]["sunrise"]) + country_time_zone
                sun_set_time = int(response_api["sys"]["sunset"]) + country_time_zone
                lol = """ 
                WEATHER INFO GATHERED
                Location: {}
                Temperature ☀️: {}°С
                    minimium: {}°С
                    maximum : {}°С
                Humidity 🌤**: {}%
                Wind 💨: {}m/s
                Clouds ☁️: {}hpa
                Sunrise 🌤: {} {}
                Sunset 🌝: {} {}""".format(
                    input_str,
                    response_api["main"]["temp"],
                    response_api["main"]["temp_min"],
                    response_api["main"]["temp_max"],
                    response_api["main"]["humidity"],
                    response_api["wind"]["speed"],
                    response_api["clouds"]["all"],
                    # response_api["main"]["pressure"],
                    time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sun_rise_time)),
                    country_code,
                    time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sun_set_time)),
                    country_code,
                )
                results.append(
                    InlineQueryResultArticle(
                        title="Weather Information",
                        description=lol,
                        input_message_content=InputTextMessageContent(
                            lol, disable_web_page_preview=True
                        ),
                    )
                )
                await client.answer_inline_query(
                    query.id, cache_time=0, results=results
                )

        elif text.split()[0] == "datetime":
            results = []
            gay = text.split(None, 1)[1]
            lel = gay
            query_timezone = lel.lower()
            if len(query_timezone) == 2:
                result = generate_time(query_timezone, ["countryCode"])
            else:
                result = generate_time(query_timezone, ["zoneName", "countryName"])

            if not result:
                result = f"Timezone info not available for <b>{lel}</b>"

            results.append(
                InlineQueryResultArticle(
                    title=f"Date & Time info of {lel}",
                    description=result,
                    input_message_content=InputTextMessageContent(
                        result, disable_web_page_preview=False, parse_mode="html"
                    ),
                )
            )
            await client.answer_inline_query(query.id, cache_time=0, results=results)

        elif text.split()[0] == "app":
            rip = []
            app_name = text.split(None, 1)[1]
            remove_space = app_name.split(" ")
            final_name = "+".join(remove_space)
            page = requests.get(
                "https://play.google.com/store/search?q=" + final_name + "&c=apps"
            )
            str(page.status_code)
            soup = BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
            results = soup.findAll("div", "ZmHEEd")
            app_name = (
                results[0]
                .findNext("div", "Vpfmgd")
                .findNext("div", "WsMG1c nnK0zc")
                .text
            )
            app_dev = (
                results[0].findNext("div", "Vpfmgd").findNext("div", "KoLSrc").text
            )
            app_dev_link = (
                "https://play.google.com"
                + results[0].findNext("div", "Vpfmgd").findNext("a", "mnKHRc")["href"]
            )
            app_rating = (
                results[0]
                .findNext("div", "Vpfmgd")
                .findNext("div", "pf5lIe")
                .find("div")["aria-label"]
            )
            app_link = (
                "https://play.google.com"
                + results[0]
                .findNext("div", "Vpfmgd")
                .findNext("div", "vU6FJ p63iDd")
                .a["href"]
            )
            app_icon = (
                results[0]
                .findNext("div", "Vpfmgd")
                .findNext("div", "uzcko")
                .img["data-src"]
            )
            app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
            app_details += " <b>" + app_name + "</b>"
            app_details += (
                "\n\n<code>Developer :</code> <a href='"
                + app_dev_link
                + "'>"
                + app_dev
                + "</a>"
            )
            app_details += "\n<code>Rating :</code> " + app_rating.replace(
                "Rated ", "⭐ "
            ).replace(" out of ", "/").replace(" stars", "", 1).replace(
                " stars", "⭐ "
            ).replace(
                "five", "5"
            )
            app_details += (
                "\n<code>Features :</code> <a href='"
                + app_link
                + "'>View in Play Store</a>"
            )
            app_details += f"\n\n===> @{SUPPORT_CHAT} <==="
            rip.append(
                InlineQueryResultArticle(
                    title=f"Datails of {app_name}",
                    description=app_details,
                    input_message_content=InputTextMessageContent(
                        app_details, disable_web_page_preview=True, parse_mode="html"
                    ),
                )
            )
            await client.answer_inline_query(query.id, cache_time=0, results=rip)

        elif text.split()[0] == "gh":
            results = []
            gett = text.split(None, 1)[1]
            text = gett + ' "site:github.com"'
            gresults = await GoogleSearch().async_search(text, 1)
            result = ""
            for i in range(4):
                try:
                    title = gresults["titles"][i].replace("\n", " ")
                    source = gresults["links"][i]
                    description = gresults["descriptions"][i]
                    result += f"[{title}]({source})\n"
                    result += f"`{description}`\n\n"
                except IndexError:
                    pass
            results.append(
                InlineQueryResultArticle(
                    title=f"Results for {gett}",
                    description=f" Github info of {title}\n  Touch to read",
                    input_message_content=InputTextMessageContent(
                        result, disable_web_page_preview=True
                    ),
                )
            )
            await client.answer_inline_query(query.id, cache_time=0, results=results)

        elif text.split()[0] == "so":
            results = []
            gett = text.split(None, 1)[1]
            text = gett + ' "site:stackoverflow.com"'
            gresults = await GoogleSearch().async_search(text, 1)
            result = ""
            for i in range(4):
                try:
                    title = gresults["titles"][i].replace("\n", " ")
                    source = gresults["links"][i]
                    description = gresults["descriptions"][i]
                    result += f"[{title}]({source})\n"
                    result += f"`{description}`\n\n"
                except IndexError:
                    pass
            results.append(
                InlineQueryResultArticle(
                    title=f"Stack overflow saerch - {title}",
                    description=f" Touch to view search results on {title}",
                    input_message_content=InputTextMessageContent(
                        result, disable_web_page_preview=True
                    ),
                )
            )
            await client.answer_inline_query(query.id, cache_time=0, results=results)

    except (IndexError, TypeError, KeyError, ValueError):
        return


def generate_time(to_find: str, findtype: List[str]) -> str:
    data = requests.get(
        f"http://api.timezonedb.com/v2.1/list-time-zone"
        f"?key={TIME_API_KEY}"
        f"&format=json"
        f"&fields=countryCode,countryName,zoneName,gmtOffset,timestamp,dst"
    ).json()

    for zone in data["zones"]:
        for eachtype in findtype:
            if to_find in zone[eachtype].lower():
                country_name = zone["countryName"]
                country_zone = zone["zoneName"]
                country_code = zone["countryCode"]

                if zone["dst"] == 1:
                    daylight_saving = "Yes"
                else:
                    daylight_saving = "No"

                date_fmt = r"%d-%m-%Y"
                time_fmt = r"%H:%M:%S"
                day_fmt = r"%A"
                gmt_offset = zone["gmtOffset"]
                timestamp = datetime.datetime.now(
                    datetime.timezone.utc
                ) + datetime.timedelta(seconds=gmt_offset)
                current_date = timestamp.strftime(date_fmt)
                current_time = timestamp.strftime(time_fmt)
                current_day = timestamp.strftime(day_fmt)

                break

    try:
        result = (
            f" DATE AND TIME OF COUNTRY"
            f"🌍Country :{country_name}\n"
            f"⏳Zone Name : {country_zone}\n"
            f"🗺Country Code: {country_code}\n"
            f"🌞Daylight saving : {daylight_saving}\n"
            f"🌅Day : {current_day}\n"
            f"⌚Current Time : {current_time}\n"
            f"📆Current Date :{current_date}"
        )
    except BaseException:
        result = None

    return result
