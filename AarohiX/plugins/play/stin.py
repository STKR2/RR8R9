from pyrogram import (Client ,filters)
from datetime import (date)
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,ForceReply,CallbackQuery)
from pyromod import listen
import sqlite3,os,time
from AarohiX import app
from config import OWNER_ID 
con = sqlite3.connect(database="b3KkK.db",check_same_thread=False)
db = con.cursor()

db.execute('''CREATE TABLE IF NOT EXISTS TWSEL (chat_id INTEGER PRIMARY KEY)''')
db.execute('''CREATE TABLE IF NOT EXISTS USERS (user_id INTEGER PRIMARY KEY)''')
db.execute('''CREATE TABLE IF NOT EXISTS BAN_USERS (user_id INTEGER PRIMARY KEY)''')
con.commit()


def GET_USERS() -> str:
	USERS = []
	try:
		db.execute("SELECT * FROM USERS")
		for USER in db.fetchall():
			USERS.append(USER[0])
		return USERS
	except:
		return []

def GET_BAN_USERS() -> str:
	BAN_USERS = []
	try:
		db.execute("SELECT * FROM BAN_USERS")
		for USER in db.fetchall():
			BAN_USERS.append(USER[0])
		return BAN_USERS
	except:
		return []

def CHECK_BAND(user_id:int) -> str:
	db.execute("SELECT user_id FROM BAN_USERS WHERE user_id = ?",(user_id,))
	return bool(db.fetchall())

def ADD_BAN(user_id:int):
	if CHECK_BAND(user_id=user_id):
		return
	db.execute("INSERT INTO BAN_USERS(user_id) VALUES(?)",(user_id,))
	con.commit()

def DEL_BAN(user_id:int):
	if not CHECK_BAND(user_id=user_id):
		return
	db.execute("DELETE FROM BAN_USERS WHERE user_id = ?",(user_id,))
	con.commit()


REB = ReplyKeyboardMarkup([
	[("تفعيل التواصل"),("تعطيل التواصل")],
	[("الاحصائيات"),("اذاعه للكل")],
	[("الغاء حظر عضو"),("حظر عضو")],
	[("الغاء")]],
	resize_keyboard=True)

@app.on_message(filters.command("start") & filters.private)
async def START(c:Client,m:Message):
	UserName = m.from_user.username
	UserName = "@"+UserName if UserName else "There in no username"
	db.execute("SELECT * FROM USERS WHERE user_id = ?", (m.from_user.id,))
	result = db.fetchone()
	
	if m.from_user.id == OWNER_ID:
		await m.reply("اليك لوحه المطور",reply_markup=REB,quote=True)
	elif CHECK_BAND(user_id=m.from_user.id):
		await m.reply("**تم حظرك من استخدام البوت**",quote=True)
	elif result:
		await m.reply(f"""
		مرحبا {m.from_user.mention}
	
	في بوت التواصل الخاص بي
	ارسل رسالتك وسيتم الرد عليك قريبا
		""",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("Dev",user_id=OWNER_ID)]]),quote= True)
	else:
		db.execute("INSERT INTO USERS(user_id) VALUES(?)", (m.from_user.id,))
		con.commit()
		try:
			await b3kkk.send_message(OWNER_ID, f"""
		<u>«**New User**»</u>
		
	➣ Name : {m.from_user.first_name}
	➣ User Name : {UserName}
	➣ User Id : `{m.from_user.id}`
	➣ Link : [Link Profile](tg://user?id={m.from_user.id})
	➣ Data : **{date.today()}**
		""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(m.from_user.first_name, user_id=m.from_user.id)], [InlineKeyboardButton("حظر هذا العضو", callback_data=f"Ban:{m.from_user.id}")]]))
	        except:pass
		await m.reply(f"""
		مرحبا {m.from_user.mention}
	
	في بوت التواصل الخاص بي
	ارسل رسالتك وسيتم الرد عليك قريبا
		""",reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton ("Dev",user_id=OWNER_ID)]]),quote= True)
		

	
@app.on_message(filters.command("تفعيل التواصل","") & filters.user(OWNER_ID) & filters.private)
async def OnTw(c:Client,m:Message):
	db.execute("SELECT * FROM TWSEL WHERE chat_id = ?", (m.chat.id,))
	result = db.fetchone()
	if result:
		await m.reply(f"مطوري {m.from_user.mention}\nتم تفعيل التواصل من قبل",quote=True)
	else:
		db.execute("INSERT INTO TWSEL(chat_id) VALUES(?)", (m.chat.id,))
		con.commit()
		await m.reply(f"مطوري {m.from_user.mention}\nتم تفعيل التواصل",quote=True)

@app.on_message(filters.command("تعطيل التواصل","") & filters.user(OWNER_ID) & filters.private)
async def OffTw(c:Client,m:Message):
	db.execute("SELECT * FROM TWSEL WHERE chat_id = ?", (m.chat.id,))
	result = db.fetchone()
	
	if result is not None:
		db.execute("DELETE FROM TWSEL WHERE chat_id = ?", (m.chat.id,))
		con.commit()
		await m.reply(f"مطوري {m.from_user.mention}\nتم تعطيل التواصل",quote=True)
	else:
		await m.reply(f"مطوري {m.from_user.mention}\nتم تعطيل التواصل من قبل",quote=True)


@app.on_message(filters.command("الاحصائيات","") & filters.user(OWNER_ID) & filters.private)
async def StatTw(c:Client,m:Message):
	Wait = await m.reply("Wait a second")
	time.sleep(.5)
	Users = GET_USERS()
	with open("Users.txt","w") as file:
		for User in Users:
			file.write(str(User)+"\n")
	READ = open("Users.txt","rb")
	Users = GET_BAN_USERS()
	with open("Ban_Users.txt","w") as file:
		for User in Users:
			file.write(str(User)+"\n")
	READ2 = open("Ban_Users.txt","rb")
	await Wait.delete()
	try:	
		await m.reply_document(READ,caption="**<u>➣ User Stats  </u>**")
		os.remove("Users.txt")
	except:os.remove("Users.txt")
	try:	
		await m.reply_document(READ2,caption="**<u>➣ Ban User Stats  </u>**")
		os.remove("Ban_Users.txt")
	except:os.remove("Ban_Users.txt")


@app.on_message(filters.command("اذاعه للكل","") & filters.user(OWNER_ID) & filters.private)
async def Broad(c:Client,m:Message):
	db.execute("SELECT * FROM USERS")
	users = len(db.fetchall())
	con.commit()
	if users < 1:
		await m.reply("➣**<u>لا يوجد مستخدمين ليتم الاذاعه لهم</u>**")
	else:
		Msg = await m.chat.ask("**ارسل الان نص الاذاعه**\nللالغاء ارسل `الغاء` اضغط للنسخ",
		reply_markup=ForceReply())
		if Msg.text == "الغاء":
			return await m.reply("**تم الغاء الاذاعه**",reply_markup=REB)
		REP = await m.reply("**انتظر يتم الاذاعه الان**")
		for user in GET_USERS():
			try:
				await Msg.copy(int(user))
			except:pass
		await REP.delete()
		await m.reply(f"➣\n**<u> تم الاذاعه الي {users} من الاعضاء</u>**",reply_markup=REB)


@app.on_message(filters.command("حظر عضو","") & filters.user(OWNER_ID) & filters.private)
async def Ban(c:Client,m:Message):
	Msg = await m.chat.ask("**ارسل الان ايدي العضو المراد حظره**",reply_markup=ForceReply())
	if Msg.text == "الغاء":
		return await m.reply("**تم الغاء الامر**",reply_markup=REB)
	if Msg.text == m.from_user.id:
		return await m.reply("**لا يمكنك حظر نفسك**")
	try:
		if CHECK_BAND(user_id=Msg.text):
			return await m.reply("**هذا المستخدم محظور من قبل**",reply_markup=REB)
	except ValueError:
		return await m.reply("**ارسل ايدي صالح للاستخدام في التلجرام**",reply_markup=REB)
	try:
		ADD_BAN(user_id=int(Msg.text))
		return await m.reply(f"**تم حظر {Msg.text} من البوت",reply_markup=REB)
	except ValueError:
		return await m.reply("**ارسل ايدي صالح للاستخدام في التلجرام**",reply_markup=REB)
	
@app.on_message(filters.command("الغاء حظر عضو","") & filters.user(OWNER_ID) & filters.private)
async def UnBan(c:Client,m:Message):
	Msg = await m.chat.ask("**ارسل الان ايدي العضو المراد الغاء حظره**",reply_markup=ForceReply())
	if Msg.text == "الغاء":
		return await m.reply("**تم الغاء الامر**",reply_markup=REB)
	if Msg.text == m.from_user.id:
		return await m.reply("**لا يمكنك الغاء حظر نفسك**")
	try:
		if not CHECK_BAND(user_id=Msg.text):
			return await m.reply("**هذا المستخدم لم يتم حظره من قبل**",reply_markup=REB)
	except ValueError:
		return await m.reply("**ارسل ايدي صالح للاستخدام في التلجرام**",reply_markup=REB)
	try:
		DEL_BAN(user_id=int(Msg.text))
		return await m.reply(f"**تم الغاء حظر {Msg.text} من البوت",reply_markup=REB)
	except ValueError:
		return await m.reply("**ارسل ايدي صالح للاستخدام في التلجرام**",reply_markup=REB)
	try:
		await b3kkk.send_message(Msg.text,f"**مرحبا {Msg.text} تم الغاء حظرك من البوت بنجاح")
	except:pass


@app.on_message(filters.private & ~filters.command("start") & ~filters.user(5565674333))
async def Private(c:Client,m:Message):
	db.execute("SELECT * FROM TWSEL WHERE chat_id = ?", (m.chat.id,))
	result = db.fetchone()
	
	if CHECK_BAND(user_id=m.from_user.id):
		await m.reply("**تم حظرك من استخدام البوت**",quote=True)
	elif result is None:
		await m.reply("**عذرا التواصل معطل من قبل مطور البوت**",quote=True)
	else:
		await b3kkk.copy_message(chat_id=OWNER_ID,
		from_chat_id=m.chat.id,message_id=m.id,
		reply_markup=InlineKeyboardMarkup([[
		InlineKeyboardButton (m.from_user.first_name,
		user_id=m.from_user.id)],[
		InlineKeyboardButton("الرد علي العضو",
		callback_data=f"Reply:{m.from_user.id}")],[
		InlineKeyboardButton("حظر هذا العضو",
		callback_data=f"Ban:{m.from_user.id}")]
		]))
		await m.reply("**تم استلام رسالتك انتظر الرد**",quote=True)

@app.on_callback_query(filters.regex(f"Ban:") & ~filters.regex(f"Reply:"))
async def BanInli(c: Client, query: CallbackQuery):
	ID = int(query.data.split(":")[1])
	KEY = InlineKeyboardMarkup([[
	InlineKeyboardButton ("الدخول للعضو المحظور",user_id=ID)]])
	ADD_BAN(user_id=ID)
	try:
		await query.message.edit_text(f"**تم حظر `{ID}` من البوت**",reply_markup=KEY)
	except:pass

@app.on_callback_query(~filters.regex(f"Ban:") & filters.regex(f"Reply:"))
async def Reply(c: Client, query: CallbackQuery):
	ID = int(query.data.split(":")[1])
	
	a = await query.message.chat.ask("** ارسل الان مضون الرساله لارسلها للشخص**")
	
	try:
		await b3kkk.send_message(chat_id=ID, text=str(a.text))
		await query.message.reply("**تم ارسال رسالتك**",quote=True)
	except Exception as e:
			await query.message.reply("**يسمح فقط بارسال نص فقط ولا يمسح باي شي ثاني\n\nError:**\n"+str(e))
	
			
