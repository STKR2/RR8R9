from pyrogram import * 
from pyrogram.types import * 
from pyromod import listen
import time
import requests

api_id = 8934899 
api_hash = "bf3e98d2c351e4ad06946b4897374a1e"
token = "5793326527:AAG1L2hrzf_9sPOL-cSueat_zOh_QE6E43s"

bot_id = token.split(":")[0]

owner = int(1854384004)

try:
	open(f"Users{bot_id}.json","r")
except FileNotFoundError:
	open(f"Users{bot_id}.json","w")
try:
	open(f"sudo{bot_id}.json","r")
except FileNotFoundError:
	open(f"sudo{bot_id}.json","w")
try:
	open(f"maindevs{bot_id}.json","r")
except FileNotFoundError:
	open(f"maindevs{bot_id}.json","w")
try:
	open(f"maindevsVII{bot_id}.json","r")
except FileNotFoundError:
	open(f"maindevsVII{bot_id}.json","w")
try:
	open(f"groups{bot_id}.json","r")
except FileNotFoundError:
	open(f"groups{bot_id}.json","w")
try:
	open(f"band{bot_id}.json","r")
except FileNotFoundError:
	open(f"band{bot_id}.json","w")
try:
	open(f"links{bot_id}.json","r")
except FileNotFoundError:
	open(f"links{bot_id}.json","w")
try:
	open(f"channel{bot_id}.json","r")
except FileNotFoundError:
	open(f"channel{bot_id}.json","w")
try:
	open(f"devchannel{bot_id}.json","r")
except FileNotFoundError:
	open(f"devchannel{bot_id}.json","w")
try:
	open(f"devuser{bot_id}.json","r")
except FileNotFoundError:
	open(f"devuser{bot_id}.json","w")
try:
	open(f'owner{bot_id}.json','r')
except FileNotFoundError:
	f = open(f'owner{bot_id}.json','w')
	f.write(str(owner))
	

	
source_ch = "vvyvv6"

app = Client("N00",api_id=api_id,api_hash=api_hash,bot_token=token)

start_text = "**welcome {} , its just a test bot √**"



OwnerM = ReplyKeyboardMarkup([
[("رفع مالك"),("تنزيل مالك"),("المالكين"),("حذف المالكين")],
[("الغاء")], 
[("◍ قسم الاحصائيات ◍")],
[("الاحصائيات"),("نسخه الكل")],
[("عرض المجموعات"),("عدد المجموعات"),("نسخه المجموعات"),("روابط المجموعات")],
[("عرض الاساسيين"),("عرض الاعضاء"),("عرض المحظورين"),("عرض المطورين")], 
[("عدد الاساسيين"),("عدد الاعضاء"),("عدد المحظورين"),("عدد المطورين")], 
[("نسخه الاساسيين"),("نسخه الاعضاء"),("نسخه المحظورين"),("نسخه المطورين")],

[("-")], 

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموعات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموعات"),("توجيه محظورين")],
[("الغاء")], 


[("◍ قسم الاساسيين"),("◍ قسم المطورين"),("◍ قسم الحظر ◍")],
[("رفع مطور اساسي"),("رفع مطور"),("حظر عضو")],
[("تنزيل مطور اساسي"),("تنزيل مطور"),("الغاء حظر عضو")],
[("عرض المطورين الاساسيين"),("عرض المطورين"),("عرض المحظورين")],
[("حذف الاساسيين"),("حذف المطورين"),("حذف المحظورين")],
[("الغاء")],

[("◍ قسم الاشتراك ◍"),("◍ قسم معرف المطور ◍"),("◍ قسم المطور ◍")],
[("عرض قناة الاشتراك"),("عرض معرف المطور"),("عرض قناة المطور")],
[("اضف قناة اشتراك اجباري"),("اضافه معرف المطور"),("اضافه قناه المطور")],
[("حذف قناه الاشتراك"),("حذف معرف المطور"),("حذف قناه المطور")],
[("الغاء")], 
[("•---- حذف الكيبورد -----•")]
])

mainSudoVIIM = ReplyKeyboardMarkup([
[("•---- حذف الكيبورد -----•")],
[("◍ قسم الاحصائيات ◍")],
[("الاحصائيات")],
[("عرض المجموعات"),("عدد المجموعات"),("نسخه المجموعات"),("نسخه للكل")],
[("عرض الاساسيين"),("عرض الاعضاء"),("عرض المحظورين"),("عرض المطورين")], 
[("عدد الاساسيين"),("عدد الاعضاء"),("عدد المحظورين"),("عدد المطورين")], 
[("نسخه الاساسيين"),("نسخه الاعضاء"),("نسخه المحظورين"),("نسخه المطورين")],

[("-")], 

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموعات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموعات"),("توجيه محظورين")],
[("الغاء")], 


[("◍ قسم الاساسيين"),("◍ قسم المطورين"),("◍ قسم الحظر ◍")],
[("رفع مطور اساسي"),("رفع مطور"),("حظر عضو")],
[("تنزيل مطور اساسي"),("تنزيل مطور"),("الغاء حظر عضو")],
[("عرض المطورين الاساسيين"),("عرض المطورين"),("عرض المحظورين")],
[("حذف الاساسيين"),("حذف المطورين"),("حذف المحظورين")],
[("الغاء")],

[("◍ قسم الاشتراك ◍"),("◍"),("◍ قسم المطور ◍")],
[("عرض قناة الاشتراك"),("-"),("عرض قناة المطور")],
[("اضف قناة اشتراك اجباري"),("-"),("اضافه قناه المطور")],
[("حذف قناه الاشتراك"),("-"),("حذف قناه المطور")],
[("الغاء")], 
[("•---- حذف الكيبورد -----•")]
])


main_dev_key = ReplyKeyboardMarkup([
[("•---- حذف الكيبورد -----•")],
[("◍ قسم الاحصائيات ◍")],
[("الاحصائيات")],
[("عرض المجموعات"),("عدد المجموعات"),("نسخه المجموعات"),("نسخه للكل")],
[("عرض الاساسيين"),("عرض الاعضاء"),("عرض المحظورين"),("عرض المطورين")], 
[("عدد الاساسيين"),("عدد الاعضاء"),("عدد المحظورين"),("عدد المطورين")], 
[("نسخه الاساسيين"),("نسخه الاعضاء"),("نسخه المحظورين"),("نسخه المطورين")],

[("-")], 

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموعات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموعات"),("توجيه محظورين")],
[("الغاء")], 


[("◍ قسم الاساسيين"),("◍ قسم المطورين"),("◍ قسم الحظر ◍")],
[("رفع مطور اساسي"),("رفع مطور"),("حظر عضو")],
[("تنزيل مطور اساسي"),("تنزيل مطور"),("الغاء حظر عضو")],
[("عرض المطورين الاساسيين"),("عرض المطورين"),("عرض المحظورين")],
[("الغاء")],

[("•---- حذف الكيبورد -----•")]
])

sudo_keyboard = ReplyKeyboardMarkup([
[("•---- حذف الكيبورد -----•")],
[("◍ قسم الاحصائيات ◍")],
[("الاحصائيات"),("نسخه")],
[("عرض المجموعات"),("نسخه للجروبات"),("عدد الجروبات")],
[("عرض روابط المجموعات"),("نسخه للمحظورين")],
[("عرض الاعضاء"),("عرض المطورين")], 
[("عدد الاعضاء"),("عدد المطورين")], 
[("نسخه الاعضاء"),("نسخه المطورين")],

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموعات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموعات"),("توجيه محظورين")],
[("الغاء")], 

[("◍ قسم الحظر ◍")],
[("حظر عضو "),("الغاء حظر عضو"),("عرض المحظورين")],
[("•---- حذف الكيبورد -----•")]
])




def is_user(id):
	result = False
	file = open(f"Users{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result

def is_dev(id):
	result = False
	file = open(f"sudo{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result
	
def del_all_sudo():
	open(f"sudo{bot_id}.json","w")

def del_all_main():
	open(f"maindevs{bot_id}.json","w")

def del_all_mainVII():
	open(f"maindevsVII{bot_id}.json","w") 
	
def del_all_ban():
	open(f"band{bot_id}.json","w")

def is_main_dev(id):
	result = False
	file = open(f"maindevs{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result
	
def is_main_devVII(id):
	result = False
	file = open(f"maindevsVII{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result
	
def is_band(id):
	result = False
	file = open(f"band{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return  result
	
def is_group(id):
	result = False
	file = open(f"groups{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result

def add_user(id):
	file = open(f"Users{bot_id}.json","a")
	file.write("{}\n".format(id))

def show_channel() -> str:
	with open(f"channel{bot_id}.json","r") as file:
		return file.readline()

def add_channel(chat_id):
	with open(f"channel{bot_id}.json","w") as file:
		file.write(chat_id)

def del_channel():
	open(f"channel{bot_id}.json","w")

def get_bot_owner() -> int:
	with open("owner{bot_id}.json","r") as file:
		return file.readline()
		
def set_bot_owner(user_id:int):
	with open(f"owner{bot_id}.json","w") as file:
		file.write(str(user_id))

def show_devchannel() -> str:
	with open(f"devchannel{bot_id}.json","r") as file:
		return file.readline()

def add_devchannel(chat_id):
	with open(f"devchannel{bot_id}.json","w") as file:
		file.write(chat_id)

def del_devchannel():
	open(f"devchannel{bot_id}.json","w")


def show_devuser() -> str:
	with open(f"devuser{bot_id}.json","r") as file:
		return file.readline()

def add_devuser(chat_id):
	with open(f"devuser{bot_id}.json","w") as file:
		file.write(chat_id)

def del_devuser():
	open(f"devuser{bot_id}.json","w")



sudo_message = f"**💌╖اهلا بيك حبيبي آلمـطـور\n⚙️╢ تقدر تتحكم باوامر البوت عن طريق\n🔍╢ الكيبور اللي ظهرتلك تحت ↘️\n🔰╜ للدخول لقناة السورس @{show_devchannel()}**"


start_buttons = InlineKeyboardMarkup([[
InlineKeyboardButton("ch",url=f"https://t.me/{show_devchannel()}")
]])


New_Member = """**
دخل عضو جديد للبوت 🪄🪄

᥀︙حسابة : {} 
᥀︙ايديه : `{}`

Time : {} .

**"""
	
dev_ch_bu = InlineKeyboardMarkup([[
InlineKeyboardButton("Dev",user_id=owner),
InlineKeyboardButton("Ch",url=f"https://t.me/{show_devchannel()}")
]])



@app.on_message(filters.command("start")&filters.private)
async def app_start(c:Client,m:Message):
	do = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{show_channel()}&user_id={m.from_user.id}").text
	user = m.from_user.id
	mm = m.from_user.mention
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	Sudo = open(f"sudo{bot_id}.json","r").read()
	banD = open(f"band{bot_id}.json","r").read()
	
	if do.count("left") or do.count("Bad Request: user not found") or is_user(id=user) and not is_band(user):
          await m.reply_text(f"**Join [this channel](t.me/{show_channel()}) first to be able to use the bot**",disable_web_page_preview=True,reply_markup=InlineKeyboardMarkup(
[[
InlineKeyboardButton("Join Channel",
url=f'https://t.me/{show_channel()}'),
],
]))
	
	else:
	    await app.send_message(text=f"Hi {m.from_user.mention}",
	    chat_id = m.chat.id, 
        reply_to_message_id=m.id,
      disable_web_page_preview = True)
	
	
	if str(user) in banD:
		return await m.reply(f"**◍ عذرا {mm} انت محظور من استخدام البوت \n√**",reply_markup=dev_ch_bu)
		
	if user == owner:
		return await m.reply(f"💌╖اهلا بيك حبيبي آلمـطـور الاساسي\n⚙️╢ تقدر تتحكم باوامر البوت عن طريق\n🔍╢ الكيبور اللي ظهرتلك تحت ↘️\n🔰╜ للدخول لقناة السورس @{show_devchannel()}",reply_markup=OwnerM)
	
	if str(user) in mainSudoVII:
		return await m.reply(f"💌╖اهلا بيك حبيبي آلمـطـور الاساسي\n⚙️╢ تقدر تتحكم باوامر البوت عن طريق\n🔍╢ الكيبور اللي ظهرتلك تحت ↘️\n🔰╜ للدخول لقناة السورس @{show_devchannel()}",reply_markup=mainSudoVIIM)
	
	if str(user) in mainSudo:
		return await m.reply(f"💌╖اهلا بيك حبيبي آلمـطـور الاساسي\n⚙️╢ تقدر تتحكم باوامر البوت عن طريق\n🔍╢ الكيبور اللي ظهرتلك تحت ↘️\n🔰╜ للدخول لقناة السورس @{show_devchannel()}",reply_markup=main_dev_key)
	
	if str(user) in Sudo:
		return await m.reply(sudo_message,reply_markup=sudo_keyboard)
	
	if is_user(id=user) and not is_band(user):
		return await m.reply(start_text,reply_markup=start_buttons)
		
	if (not is_user(id=str(user))):
		add_user(id=user)
		cc = time.strftime("%H : %M : %S")
		try:
			await app.send_message(owner,New_Member.format(mm,user,cc),
			reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("دخول لحسابه",
			user_id=int(user))]]))
		except:
			await app.send_message(owner,"**دخل عضو جديد للبوت ولم استطع تحديد معلوماته √**")
	
@app.on_message(filters.command("الاحصائيات","")&filters.private)
async def __count(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if  str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		users = len(open(f"Users{bot_id}.json","r").readlines())
		groups = len(open(f"groups{bot_id}.json","r").readlines())
		sudos = len(open(f"sudo{bot_id}.json","r").readlines())
		main = len(open(f"maindevs{bot_id}.json","r").readlines())
		bans = len(open(f"band{bot_id}.json","r").readlines())
		
		msg = f"""
		**◍ Bot Status : **
			
		├ users : {users} 
		├ sudos : {sudos} 
		├ groups : {groups} 
		├ main sudos : {main} 
		├ band  {bans} 
		
		√ """
		return await m.reply(msg,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("close",callback_data="close")]]))
	return await m.reply("**◍ انت لست مطور في البوت \n√**")
	
@app.on_callback_query(filters.regex("close"))
async def close__(_,query:CallbackQuery):
	user = query.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		await query.message.delete()
		
	else:
		await query.answer("❎ فقط المطورين من لديهم الحق في القيام بهذا .")

@app.on_message(filters.command("•---- حذف الكيبورد -----•","")&filters.private)
async def del_keyboard(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		return await m.reply("**◍ تم حذف الكيبورد بنجاح  /start\n√**",reply_markup=ReplyKeyboardRemove())
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_message(filters.command("^نسخه الكل$","")&filters.private)
async def __get_copy(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		users = open(f"Users{bot_id}.json","rb")
		groups = open(f"groups{bot_id}.json","rb")
		band = open(f"band{bot_id}.json","rb")
		sudos = open(f"sudo{bot_id}.json","rb")
		main = open(f"maindevs{bot_id}.json","rb")
		
		uc = len(open(f"Users{bot_id}.json","r").readlines())
		gc = len(open(f"groups{bot_id}.json","r").readlines())
		bc = len(open(f"band{bot_id}.json","r").readlines())
		sc = len(open(f"sudo{bot_id}.json","r").readlines())
		mc = len(open(f"maindevs{bot_id}.json","r").readlines())
		
		cc = await m.reply("**◍ جاري جلب النسخه الاحتياطية \n√**")
		time.sleep(3)
		await cc.delete()
		try:
			await m.reply_document(document=users,caption=f"**Bot users : {uc} √**")
		except:
			await m.reply("**◍ لم يقم اي عضو بالدخول الي بوتك √**")
		try:
			await m.reply_document(document=groups,caption=f"**Bot groups : {gc} √**")
		except:
			await m.reply("**◍ لم يتم تفعيل اي مجموعات في بوتك √**")
		try:
			await m.reply_document(document=band,caption=f"**Band users : {bc} √**")
		except:
			await m.reply("**◍ لا يوجد اعضاء محظورين في البوت √**")
		try:
			await m.reply_document(document=sudos,caption=f"**Sudo users : {sc} √**")
		except:
			await m.reply("**◍ لا يوجد مطورين في البوت √**")
		try:
			await m.reply_document(document=main,caption=f"**Main devs : {mc} √**")
		except:
			await m.reply("**◍ لا يوجد مطورين اساسيين في البوت √**")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")
	


@app.on_message(filters.command("^عرض المجموعات$","")&filters.private)
async def show_groups(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		groups = open(f"groups{bot_id}.json")
		x = 1
		text = "**Bot groups **:\n\n"
		for gr in groups:
			text += f"{x} - {gr} \n"
			x+=1
		i =await m.reply("**◍ جاري عرض الجروبات √**")
		time.sleep(.5)
		leng = len(open(f"groups{bot_id}.json","r").readlines())
		if leng == 0:
			return await i.edit("**◍ لا توجد مجموعات تم تفعيلها في البوت √**")
		return await i.edit(text=text)
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

#--------------------------Group---------------------------

@app.on_message(filters.command("^نسخه المجموعات$","")&filters.private)
async def __gcopy(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		gr = open(f"groups{bot_id}.json","rb")
		gc = len(open(f"groups{bot_id}.json","r").readlines())
		i = await m.reply("**◍ جاري جلب نسخه للمجموعات √**")
		time.sleep(1.5)
		try:
			await i.delete()
			await m.reply_document(document=gr,caption=f"**Bot groups {gc}**")
		except:
			await i.delete()
			await m.reply("**◍ لا توجد مجموعات تم تفعيلها في البوت √**")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")
		
@app.on_message(filters.command("^عدد المجموعات$","")&filters.private)
async def get_groups_count(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		leng = len(open(f"groups{bot_id}.json","r").readlines())
		if leng == 0:
			return await m.reply("**◍ لا توجد مجموعات تم تفعيلها في البوت √**")
		return await m.reply(f"**◍ تم تفعيل {leng} مجموعة في بوتك \n√**")
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_message(filters.command("^روابط المجموعات$","")&filters.private)
async def show_links(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		x = 1
		text = "**Groups links **:\n\n"
		lenl = len(open(f"links{bot_id}.json","r").readlines())
		sl = open(f"links{bot_id}.json","r")
		for link in sl:
			text += f"{x} - {link}"
			x += 1
		l = await m.reply("**◍ جاري عرض الروابط √**")
		time.sleep(.5)
		if lenl == 0:
			return await l.edit("**◍ لا توجد مجموعات تم تفعيلها في البوت √**")
		return await l.edit(text=text)
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

#-----------------------BanUser---------------------------	
@app.on_message(filters.command("^نسخه المحظورين$","")&filters.private)
async def get_copy___band(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		file = open(f"band{bot_id}.json","rb")
		lenb = len(open(f"band{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري جلب نسخه للمحظورين √**")
		time.sleep(2)
		if lenb == 0:
			return await l.edit("**◍ لم يتم حظر اي عضو من استخدام البوت √**")
		await l.delete()
		await m.reply_document(document=file,caption=f"**Band users {lenb} √")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")


@app.on_message(filters.command("^عدد المحظورين$","")&filters.private)
async def countofuserBan(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		l = await m.reply("**◍ جاري حساب عدد الاعضاء √**")
		lens = len(open(f"band{bot_id}.json","r").readlines())
		time.sleep(.5)
		if lens == 0:
			return await l.edit("**◍ لم يدخل اي عضو للبوت حتي الآن √**")
		return await l.edit(f"**◍ عدد اعضاء بوتك {lens} √**")
	return await m.reply("**◍ انت لست مطور في البوت \n√**")


#----------------SpecialVIIUser-------------------------

@app.on_message(filters.command("عرض المطورين الاساسيين","")|filters.command("عرض الاساسيين","") &filters.private)
async def ShowMain(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in mainSudoVII or int(user) == owner:
		file = open(f"maindevs{bot_id}.json","r")
		lens = len(open(f"maindevs{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري عرض المطورين الاساسيين √**")
		x = 1
		text = "**Bot Main Users **:\n\n"
		for su in file:
			text += f"{x} - {su}"
			x += 1
		time.sleep(1)
		if lens == 0:
			return await l.edit("**◍ لم يتم رفع مطورين اساسيين في البوت √**")
		return await l.edit(text=text)
	return await m.reply("**◍ انت لست مطور في البوت \n√**")
	

@app.on_message(filters.command("^نسخه الاساسيين$","")&filters.private)
async def get_MainSudo(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in mainSudoVII or int(user) == owner:
		file = open(f"maindevs{bot_id}.json","rb")
		lenb = len(open(f"maindevs{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري جلب نسخه للمطورين الاساسيين√**")
		time.sleep(2)
		if lenb == 0:
			return await l.edit("**◍ لم تقم برفع اي مطور اساسي في البوت√**")
		await l.delete()
		await m.reply_document(document=file,caption=f"**Sudo Main Users {lenb} √")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")
	
@app.on_message(filters.command("^عدد الاساسيين$","")&filters.private)
async def countofDev(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in mainSudoVII or int(user) == owner:
		l = await m.reply("**◍ جاري حساب عدد اساسيين البوت√**")
		lens = len(open(f"maindevsVII{bot_id}.json","r").readlines())
		time.sleep(.5)
		if lens == 0:
			return await l.edit("**◍ لم تقم برفع اي مطورين اساسيين في البوت √**")
		return await l.edit(f"**◍ تم رفع {lens} مطور اساسي في البوت √**")
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

#----------------------SpecialUser-----------------------

@app.on_message(filters.command("^عرض المطورين$","")&filters.private)
async def __show_sudos(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		file = open(f"sudo{bot_id}.json","r")
		lens = len(open(f"sudo{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري عرض المطورين √**")
		x = 1
		text = "**Bot sudo Users **:\n\n"
		for su in file:
			text += f"{x} - {su}"
			x += 1
		time.sleep(1)
		if lens == 0:
			return await l.edit("**◍ لم يتم رفع مطورين في البوت √**")
		return await l.edit(text=text)
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_message(filters.command("^عدد المطورين$","")&filters.private)
async def countofsudos(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		l = await m.reply("**◍ جاري حساب عدد مطورين البوت √**")
		lens = len(open(f"sudo{bot_id}.json","r").readlines())
		time.sleep(.5)
		if lens == 0:
			return await l.edit("**◍ لم تقم برفع اي مطورين في البوت √**")
		return await l.edit(f"**◍ تم رفع {lens} مطور في البوت √**")
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_message(filters.command("^نسخه المطورين$","")&filters.private)
async def get_copy_Sudo(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		file = open(f"sudo{bot_id}.json","rb")
		lenb = len(open(f"sudo{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري جلب نسخه للمطورين√**")
		time.sleep(2)
		if lenb == 0:
			return await l.edit("**◍ لم تقم برفع اي مطور في البوت √**")
		await l.delete()
		await m.reply_document(document=file,caption=f"**Sudo users {lenb} √")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")	
	
#-------------------NormalUser-------------------------

@app.on_message(filters.command("^عرض الاعضاء$","")&filters.private)
async def show_users(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		users = open(f"Users{bot_id}.json","r")
		x = 1
		text = "**Bot Users **: \n\n"
		for us in users:
			text += f"{x} - {us} \n"
			x+=1
		i = await m.reply("**◍ جارى عرض الاعضاء √**")
		time.sleep(.5)
		lenm = len(open(f"Users{bot_id}.json","r").readlines())
		if lenm == 0:
			return await i.edit("**◍ لم يقم اي عضو بالدخول للبوت √**")
		return await i.edit(text=text)
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_message(filters.command("^نسخه الاعضاء$","")&filters.private)
async def __get_users_copy(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		l = await m.reply("**◍ جاري سحب نسخه للاعضاء √**")
		time.sleep(2)
		lenu = len(open(f"Users{bot_id}.json","r").readlines())
		users = open(f"Users{bot_id}.json","rb")
		if lenu == 0:
			return await l.edit("**◍ لم يقم اي عضو بالدخول الي البوت √**")
		await l.delete()
		await m.reply_document(document=users,caption=f"**Bot users {lenu} √**")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_message(filters.command("^عدد الاعضاء$","")&filters.private)
async def countofusers(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		l = await m.reply("**◍ جاري حساب عدد الاعضاء √**")
		lens = len(open(f"Users{bot_id}.json","r").readlines())
		time.sleep(.5)
		if lens == 0:
			return await l.edit("**◍ لم يدخل اي عضو للبوت حتي الآن √**")
		return await l.edit(f"**◍ عدد اعضاء بوتك {lens} √**")
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

#--------♡-------------Subscribe------------♡----------

@app.on_message(filters.command("اضف قناة اشتراك اجباري","")&filters.private)
async def AddKey(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
		ask = await m.chat.ask('**معرف القناه بدون @**')
		if ask.text == "الغاء":
			await ask.request.delete()
			await ask.delete()
			await m.reply(f"**تم الالغاء**")
			return
		if '@' in ask.text:
			return await m.reply('**المعرف بدون @**')
		if "ا" in ask.text:
			return await m.reply('لم يتم** التعرف**')
		add_channel(chat_id=ask.text)
		await m.reply('**تم وضع {} قناة اشتراك √**'.format(ask.text))
		return
		
@app.on_message(filters.command("عرض قناة الاشتراك","")&filters.private)
async def ShowKey(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
	    return await m.reply(f"**@{show_channel()} قناه الاشتراك**")
	

@app.on_message(filters.command("حذف قناه الاشتراك","")&filters.private)
async def DellKey(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
	    		del_channel()
	    		await m.reply(f"تم حذفها")
	
#--------------------------------------------------------------
#-----------------------DevChannel---------------------
@app.on_message(filters.command("اضافه قناه المطور","")&filters.private)
async def AddChannel(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
		ask = await m.chat.ask('**معرف قناه المطور بدون @**')
		if ask.text == "الغاء":
			await ask.request.delete()
			await ask.delete()
			await m.reply(f"**تم الالغاء**")
			return
		if '@' in ask.text:
			return await m.reply('**المعرف بدون @**')
		if 'اضافه'in ask.text:
			return await m.reply('**لم يتم التعرف**')
		add_devchannel(chat_id=ask.text)
		await m.reply('**تم وضع قناه المطور @{} √**'.format(ask.text))
		return
		
@app.on_message(filters.command("عرض قناة المطور","")&filters.private)
async def ShowDevKey(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
	    return await m.reply(f"**@{show_devchannel()} قناه المطور**")
	

@app.on_message(filters.command("حذف قناه المطور","")&filters.private)
async def DellDevKey(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
	    		del_devchannel()
	    		await m.reply('**حذفت القناه بنجاح**')

	    		

#--------------------------------------------------------------
#-----------------------DevUser-------------------------
@app.on_message(filters.command("اضافه معرف المطور","")&filters.private)
async def AddDevUser(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
		ask = await m.chat.ask('**معرف المطور بدون @**')
		if ask.text == "الغاء":
			await ask.request.delete()
			await ask.delete()
			await m.reply(f"**تم الالغاء**")
			return
		if '@' in ask.text:
			return await m.reply('**المعرف بدون @**')
		if 'اضافه'in ask.text:
			return await m.reply('**لم يتم التعرف**')
		add_devuser(chat_id=ask.text)
		await m.reply('**تم وضع معرف المطور @{} √**'.format(ask.text))
		return
		
@app.on_message(filters.command("عرض معرف المطور","")&filters.private)
async def ShowDevUser(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
	    return await m.reply(f"**@{show_devuser()} معرف المطور**")
	

@app.on_message(filters.command("حذف معرف المطور","")&filters.private)
async def DellDevUser(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
	    		del_devuser()
	    		await m.reply('**حذف المعرف بنجاح**')
	    		
#-------------------------------------------------------------
#---------------------AddOwner------------------------

@app.on_message(filters.command("رفع مالك",prefixes="")&filters.private)
async def AddOwner(c:Client,m:Message):
	user = m.from_user.id
	chat = m.chat.id	
	user = m.from_user.id
	if int(user) == owner:
		
		ask = await app.ask(chat,"**ارسل ايدي المالك**")
		if ask.text == "الغاء":
			await ask.request.delete()
			await m.delete()
			await m.reply("**تم الالغاء**")
		else:
			inputText = ask.text
			if(not is_main_dev(str(inputText))):
				AddMain2 = open(f"maindevsVII{bot_id}.json","a")
				AddMain2.write("{}\n".format(inputText))
				await m.reply("**تم رفع العضو {} مالك**".format(inputText))
				try:
					await app.send_message(int(inputText),"**مرحبا عزيزي تم رفعك مالك البوت**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
			else:
				await m.reply("**هذا العضو مالك من قبل**")


#-------------------------------------------------------------
#------------------------DelOwner-----------------------
@app.on_message(filters.command("تنزيل مالك",prefixes="")&filters.private)
async def DelOwner(c:Client,m:Message):
	user = m.from_user.id
	chat = m.chat.id	
	user = m.from_user.id
	if int(user) == owner:
		
		ask = await app.ask(chat,"**ارسل ايدي المالك**")
		inputText = ask.text
		if inputText =="الغاء":
			await ask.request.delete()
			await m.delete()
			await m.reply("**تم الالغاء**")
		else:
				with open(f"maindevsVII{bot_id}.json","r") as w:
					lines = w.readlines()
				with open(f"maindevsVII{bot_id}.json","w") as w:
					for line in lines:
						if line.strip("\n")!="{}".format(inputText):
							w.write(line)
				await m.reply("**تم حذف {} من المالكين**".format(inputText))
				try:
					await app.send_message(int(inputText),"**مرحبا عزيزي تم حذفك من المالكين**",
					reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
	else:
				        if(not is_dev(str(inputText))):
				            await m.reply("**ليس مطور مالك في البوت**")


#-------------------------------------------------------------
#------------------------ShowMain---------------------  

@app.on_message(filters.command("المالكين","") &filters.private)
async def ShowOwner(c:Client,m:Message):
	user = m.from_user.id
	
	if int(user) == owner:
		file = open(f"maindevsVII{bot_id}.json","r")
		lens = len(open(f"maindevsVII{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري عرض المطورين الاساسيين √**")
		x = 1
		text = "**Bot Owner Users **:\n\n"
		for su in file:
			text += f"{x} - {su}"
			x += 1
		time.sleep(1)
		if lens == 0:
			return await l.edit("**◍ لم يتم رفع مالكين في البوت√**")
		return await l.edit(text=text)
	return await m.reply("**◍ انت لست مطور في البوت \n√**")				        

#-------------------------------------------------------------
#----------------------DelAllOwner---------------------
@app.on_message(filters.command("حذف المالكين","")&filters.private)
async def DelAllOwner(c:Client,m:Message):
	user = m.from_user.id
	if int(user) == owner:
	    del_all_mainVII()
	    await m.reply(f"**تم الحذف**")		        


#-------------------------------------------------------------
#-------------------------AddMain------------------------
@app.on_message(filters.command("رفع مطور اساسي",prefixes="")&filters.private)
async def AddMain(c:Client,m:Message):
	user = m.from_user.id
	chat = m.chat.id	
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudo or str(user) in mainSudoVII or int(user) == owner:
		
		ask = await app.ask(chat,"**ارسل ايدي المطور الاساسي ")
		if ask.text == "الغاء":
			await ask.request.delete()
			await m.delete()
			await m.reply("**تم الالغاء**")
		else:
			inputText = ask.text
			if(not is_main_dev(str(inputText))):
				AddMain2 = open(f"maindevs{bot_id}.json","a")
				AddMain2.write("{}\n".format(inputText))
				await m.reply("**تم رفع العضو {} مطور اساسي**".format(inputText))
				try:
					await app.send_message(int(inputText),"**مرحبا عزيزي تم رفعك مطور اساسي في البوت**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
			else:
				await m.reply("**هذا العضو مطور اساسي من قبل**")


#-------------------------------------------------------------
#-------------------------DelMain-----------------------
@app.on_message(filters.command("تنزيل مطور اساسي",prefixes="")&filters.private)
async def DelMain(c:Client,m:Message):
	user = m.from_user.id
	chat = m.chat.id	
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudo or str(user) in mainSudoVII or int(user) == owner:
		
		ask = await app.ask(chat,"**ارسل ايدي المطور الاساسي**")
		inputText = ask.text
		if inputText =="الغاء":
			await ask.request.delete()
			await m.delete()
			await m.reply("**تم الالغاء**")
		else:
				with open(f"maindevs{bot_id}.json","r") as w:
					lines = w.readlines()
				with open(f"maindevs{bot_id}.json","w") as w:
					for line in lines:
						if line.strip("\n")!="{}".format(inputText):
							w.write(line)
				await m.reply("**تم حذف {} من المطورين الاساسيين**".format(inputText))
				try:
					await app.send_message(int(inputText),"**مرحبا عزيزي تم حذفك من المطوريين الاساسيين**",
					reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
	else:
				        if(not is_dev(str(inputText))):
				            await m.reply("**ليس مطور اساسي في البوت**")

#-------------------------------------------------------------
#-----------------------DelAllMain---------------------
@app.on_message(filters.command("حذف الاساسيين","")&filters.private)
async def DelAllMain(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	
	if str(user) in mainSudoVII or int(user) == owner:
	    del_all_main()
	await m.reply(f"**تم الحذف**")
#-------------------------------------------------------------
#-------------------------AddSudo------------------------
@app.on_message(filters.command("رفع مطور",prefixes="")&filters.private)
async def AddSudo(c:Client,m:Message):
	user = m.from_user.id
	chat = m.chat.id	
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudo or str(user) in mainSudoVII or int(user) == owner:
		
		ask = await app.ask(chat,"**ارسل ايدي المطور")
		if ask.text == "الغاء":
			await ask.request.delete()
			await m.delete()
			await m.reply("**تم الالغاء**")
		else:
			inputText = ask.text
			if(not is_main_dev(str(inputText))):
				AddMain2 = open(f"sudo{bot_id}.json","a")
				AddMain2.write("{}\n".format(inputText))
				await m.reply("**تم رفع العضو {} مطور**".format(inputText))
				try:
					await app.send_message(int(inputText),"**مرحبا عزيزي تم رفعك مطور في البوت**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
			else:
				await m.reply("**هذا العضو مطور من قبل**")


#-------------------------------------------------------------
#-------------------------DelSudo-----------------------
@app.on_message(filters.command("تنزيل مطور",prefixes="")&filters.private)
async def DelSudo(c:Client,m:Message):
	user = m.from_user.id
	chat = m.chat.id	
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudo or str(user) in mainSudoVII or int(user) == owner:
		
		ask = await app.ask(chat,"**ارسل ايدي المطور**")
		inputText = ask.text
		if inputText =="الغاء":
			await ask.request.delete()
			await m.delete()
			await m.reply("**تم الالغاء**")
		else:
				with open(f"sudo{bot_id}.json","r") as w:
					lines = w.readlines()
				with open(f"sudo{bot_id}.json","w") as w:
					for line in lines:
						if line.strip("\n")!="{}".format(inputText):
							w.write(line)
				await m.reply("**تم حذف {} من المطورين**".format(inputText))
				try:
					await app.send_message(int(inputText),"**مرحبا عزيزي تم حذفك من المطوريين**",
					reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
	else:
				        if(not is_dev(str(inputText))):
				            await m.reply("**ليس مطور في البوت**")
#-------------------------------------------------------------
#------------------------DelAllSudo---------------------
@app.on_message(filters.command("حذف المطورين","")&filters.private)
async def DelAllSudo(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	
	if str(user) in mainSudoVII or int(user) == owner:
	    del_all_sudo()
	await m.reply(f"**تم الحذف**")


#-------------------------------------------------------------
#------------------------BanUser-------------------------

@app.on_message(filters.command("حظر عضو",prefixes="")&filters.private)
async def BanUser(c:Client,m:Message):
	chat = m.chat.id
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
	 await m.delete()
	 ask = await app.ask(chat,"**ارسل ايدي العضو المراد حظره**")
	 inputText = ask.text
	 
	 if inputText == "الغاء":
	 	await ask.request.delete()
	 	await m.delete()
	 	await m.reply("**تم الالغاء**")
	 else:
			inputText = ask.text
			if(not is_band(str(inputText))):
				AddBan = open(f"band{bot_id}.json","a")
				AddBan.write("{}\n".format(inputText))
				await m.reply("**تم {} حظر العضو**".format(inputText))
	elif str(user) in sudo:
	 	with open(f"sudo{bot_id}.json","r") as w:
	 		lines = w.readlines()
	 	with open(f"sudo{bot_id}.json","w") as w:
	 		for line in lines:
	 			if line.strip("\n")!="{}".format(m.from_user.id):
	 				w.write(line)
	 	await m.reply("**يحمار بتحظر المالك\nتم تنزيل رتبتك يحمار**",
	 	reply_markup=ReplyKeyboardRemove())
	 	await app.send_message(sudo,"**حاول {} الحمار يحظرك ده يحظرك**".format(m.from_user.mention))
	 	try:
	 			await app.send_message(int(inputText),"**عزيزي تم حظرك من البوت راسل المطور لفك حظرك**",
	 			reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس",
url=f"https://t.me/{show_devchannel()}")]])
	 			)
	 	except:
	 	    pass
	 	else:
	 		await m.reply("**هذا العضو محظور من قبل**")
	 		
#-------------------------------------------------------------
#-------------------------DelBanUser--------------------

@app.on_message(filters.command("الغاء حظر عضو",prefixes="")&filters.private)
async def UnBanUser(c:Client,m:Message):
	user = m.from_user.id
	chat = m.chat.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		await m.delete()
		ask = await app.ask(chat,"**ارسل ايدي العضو**")
		inputText = ask.text
		if inputText == "الغاء":
			await ask.request.delete()
			await m.delete()
			await m.reply("**تم الغاء الحظر**")
		else:
			if(not is_band(str(inputText))):
				await m.reply("**ليس محظور بالفعل**")
			else:
				with open(f"band{bot_id}","r") as w:
					lines = w.readlines()
				with open(f"band{bot_id}","w") as w:
					for line in lines:
						if line.strip("\n")!="{}".format(inputText):
							w.write(line)
				await m.reply("**تم {} حذفه من قائمه الحظر**".format(inputText))
				try:
					await app.send_message(int(inputText),"**مرحبا عزيزي تم الغاء حظرك من البوت**",
					reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
#-------------------------------------------------------------
#---------------------ShowBanUser--------------------  

@app.on_message(filters.command("عرض المحظورين","")&filters.private)
async def ShowBan(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		file = open(f"band{bot_id}.json","r")
		lens = len(open(f"band{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري عرض المحظورين√**")
		x = 1
		text = "**Bot Ban Users **:\n\n"
		for su in file:
			text += f"{x} - {su}"
			x += 1
		time.sleep(1)
		if lens == 0:
			return await l.edit("**◍ لم يتم حظر شخص في البوت√**")
		return await l.edit(text=text)
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

#-------------------------------------------------------------
#------------------------DelAllBan---------------------

@app.on_message(filters.command("حذف المحظورين","")&filters.private)
async def DelAllBan(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	
	if str(user) in mainSudoVII or int(user) == owner:
	    del_all_ban()
	await m.reply(f"**تم الحذف**")
	
#--------------------------AllBroadCast--------------------	
@app.on_message(filters.command("اذاعه للكل",prefixes=""))
async def AllCommand__(c,m):
	user = m.from_user.id
	chat = m.chat.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		await m.delete()
		ask = await app.ask(chat,"**• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )**")
		inputText = ask.text 
		
		if inputText == "الغاء":
			await m.reply("**تم الغاء الاذاعه**")
		else:
			users = open(f"Users{bot_id}.json","r")
			groups = open(f"groups{bot_id}.json","r")
			bans = open(f"band{bot_id}.json","r")
			
			for user in users:
				try:
					await ask.copy(int(user),
					inputText,
					reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Source channel",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
				
			for group in groups:
				try:
					await ask.copy(int(group),
					inputText,
					reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Source channel",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
			
			for ban in bans:
				try:
					await ask.copy(int(ban),
					inputText,
					reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Source channel",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
				
			x1 = len(open(f"Users{bot_id}.json","r").readlines())
			x2 = len(open(f"band{bot_id}.json","r").readlines())
			x3 = len(open(f"groups{bot_id}.json","r").readlines())
			
			
			await app.send_message(chat,
			f"**تم الاذاعه الي** : \n\n {x1} من الأعضاء \n {x2} من المحظورين \n {x3} من المجموعات")


#---------------------Not Togeh----------------------------------
@app.on_message(filters.command("اذاعه الاعضاء",prefixes=""))
async def memcommands__(c,m):
	user = m.from_user.id
	chat = m.chat.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		await m.delete()
		ask = await app.ask(chat,"**• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )**")
		inputText = ask.text 
		
		if inputText == "الغاء":
			await m.reply("**تم الغاء الاذاعه**")
		
		else:
			users = open(f"Users{bot_id}.json","r")
			
			for user in users:
				try:
					await ask.copy(int(user),
					inputText, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Source channel",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
			
			us = len(open(f"Users{bot_id}.json","r").readlines())
			await app.send_message(chat,f"**تم الاذاعه الي **: \n {us} من الاعضاء")

@app.on_message(filters.command("اذاعه المحظورين",prefixes=""))
async def memcommands__(c,m):
	user = m.from_user.id
	chat = m.chat.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		await m.delete()
		ask = await app.ask(chat,"**• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )**")
		inputText = ask.text 
		
		if inputText == "الغاء":
			await m.reply("**تم الغاء الاذاعه**")
		
		else:
			band = open(f"band{bot_id}.json","r")
			
			for user in band:
				try:
					await ask.copy(int(user),
					inputText, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Source channel",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
			
			bn = len(open(f"band{bot_id}.json","r").readlines())
			await app.send_message(chat,f"**تم الاذاعه الي **: \n {bn} من المحظورين")


@app.on_message(filters.command("اذاعه المجموعات",prefixes=""))
async def memcommands__(c,m):
	user = m.from_user.id
	chat = m.chat.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		await m.delete()
		ask = await app.ask(chat,"**• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )**")
		inputText = ask.text 
		
		if inputText == "الغاء":
			await m.reply("**تم الغاء الاذاعه**")
		
		else:
			group = open(f"groups{bot_id}.json","r")
			
			for user in group:
				try:
					await ask.copy(int(user),
					inputText, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Source channel",
url=f"https://t.me/{show_devchannel()}")]])
					)
				except:
					pass
			
			gr = len(open(f"groups{bot_id}.json","r").readlines())
			await app.send_message(chat,f"**تم الاذاعه الي **: \n {gr} من الجروبات")
			
#---------------AllBroadCastTogeh----------	

@app.on_message(filters.command("توجيه للكل",prefixes=""))
async def AllCommand__(c,m):
	user = m.from_user.id
	chat = m.chat.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		await m.delete()
		ask = await app.ask(chat,"**• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )**")
		inputText = ask.text 
		
		if inputText == "الغاء":
			await m.reply("**تم الغاء الاذاعه**")
		else:
			users = open(f"Users{bot_id}.json","r")
			groups = open(f"groups{bot_id}.json","r")
			bans = open(f"band{bot_id}.json","r")
			
			for user in users:
				try:
					await ask.forward(int(user)
					)
				except:
					pass
				
			for group in groups:
				try:
					await ask.forward(int(group)
					)
				except:
					pass
			
			for ban in bans:
				try:
					await ask.forward(int(ban)
					)
				except:
					pass
				
			x1 = len(open(f"Users{bot_id}.json","r").readlines())
			x2 = len(open(f"band{bot_id}.json","r").readlines())
			x3 = len(open(f"groups{bot_id}.json","r").readlines())
			
			
			await app.send_message(chat,f"**تم الاذاعه بالتوجيه الي** : \n\n {x1} من الأعضاء \n {x2} من المحظورين \n {x3} من المجموعات")
		
#---------------------------YupTogeh---------------------------
@app.on_message(filters.command("توجيه الاعضاء",prefixes=""))
async def memcommands__(c,m):
	user = m.from_user.id
	chat = m.chat.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		await m.delete()
		ask = await app.ask(chat,"**• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )**")
		inputText = ask.text 
		
		if inputText == "الغاء":
			await m.reply("**تم الغاء الاذاعه بالتوجيه**")
		
		else:
			users = open(f"Users{bot_id}.json","r")
			
			for user in users:
				try:
					await ask.forward (int(user)
					)
				except:
					pass
			
			us = len(open(f"Users{bot_id}.json","r").readlines())
			await app.send_message(chat,f"**تم الاذاعه بالتوجيه الي **:\n {us} من الاعضاء")

@app.on_message(filters.command("توجيه محظورين",prefixes=""))
async def memcommands__(c,m):
	user = m.from_user.id
	chat = m.chat.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		await m.delete()
		ask = await app.ask(chat,"**• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )**")
		inputText = ask.text 
		
		if inputText == "الغاء":
			await m.reply("**تم الغاء الاذاعه بالتوجيه**")
		
		else:
			band = open(f"band{bot_id}.json","r")
			
			for user in band:
				try:
					await ask.copy(int(user)
					)
				except:
					pass
			
			bn = len(open(f"band{bot_id}.json","r").readlines())
			await app.send_message(chat,f"**تم الاذاعه بالتوجيه الي **: \n {bn} من المحظورين")
			
@app.on_message(filters.command("توجيه المجموعات",prefixes=""))
async def memcommands__(c,m):
	user = m.from_user.id
	chat = m.chat.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		await m.delete()
		ask = await app.ask(chat,"**• ارسل الإذاعة الآن ( صورة، ملصق، نص، متحركة، جهة اتصال، ملف )**")
		inputText = ask.text 
		
		if inputText == "الغاء":
			await m.reply("**تم الغاء الاذاعه**")
		
		else:
			group = open(f"groups{bot_id}.json","r")
			
			for user in group:
				try:
					await ask.copy(int(user)
					)
				except:
					pass
			
			gr = len(open(f"groups{bot_id}.json","r").readlines())
			await app.send_message(chat,f"**تم الاذاعه بالتوجيه الي **: \n {gr} من المحظورين")

		
app.run()
		