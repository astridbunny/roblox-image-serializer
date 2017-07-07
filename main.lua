BasePart = script.Parent.BasePart

http = game:GetService("HttpService")

response = http:GetAsync(script.Parent.URL.Value, true)

image = http:JSONDecode(response)

response = nil

BasePosition = BasePart.Position
RowStart = Vector3.new(BasePosition.X, BasePosition.Y - 0.2, BasePosition.Z)
BasePosition = RowStart
for index, row in ipairs(image) do
	for index2, pixel in ipairs(row) do
		part = BasePart:Clone()
		part.Parent = script.Parent
		part.Position = BasePosition
		part.Color = Color3.fromRGB(pixel[1], pixel[2], pixel[3])
		BasePosition = Vector3.new(BasePosition.X + 0.2, BasePosition.Y, BasePosition.Z)
	end
	RowStart = Vector3.new(RowStart.X, RowStart.Y - 0.2, RowStart.Z)
	BasePosition = RowStart
end
