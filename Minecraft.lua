local websocket = require'websocket'

--function websocketLoop()
--	
--	local ws, err = http.websocket("ws://ottomated.net:43509")
-- 
--	if err then
--		print(err)
--	elseif ws then
--		while true do
--			term.clear()
--			term.setCursorPos(1,1)
--			print("      {O}\n")
--			print("Pog Turtle OS. Do not read my code unless you are 5Head.")
--			local message = ws.receive()
--			if message == nil then
--				break
--			end
--			local obj = json.decode(message)
--			if obj.type == 'eval' then
--				local func = loadstring(obj['function'])
--				local result = func()
--				ws.send(json.encode({data=result, nonce=obj.nonce}))
--			elseif obj.type == 'mitosis' then
--				local status, res = pcall(undergoMitosis)
--				if not status then
--					ws.send(json.encode({data="null", nonce=obj.nonce}))
--				elseif res == nil then
--					ws.send(json.encode({data="null", nonce=obj.nonce}))
--				else
--					ws.send(json.encode({data=res, nonce=obj.nonce}))
--				end
--			elseif obj.type == 'mine' then
--				local status, res = pcall(mineTunnel, obj, ws)
--				ws.send(json.encode({data="end", nonce=obj.nonce}))
--			end
--		end
--	end
--	if ws then
--		ws.close()
--	end
--end

function websocketLoop()

    local ws, err = http.websocket("ws://127.0.0.1:6002")

    local ok = client:send('hello')
    if ok then
        print('msg sent')
    else
        print('connection closed')
    end

    -- receive data:

    local message,opcode = client:receive()
    if message then
        print('msg',message,opcode)
    else
        print('connection closed')
    end

    -- close connection:

    local close_was_clean,close_code,close_reason = client:close(4001,'lost interest')

    end

websocketLoop()