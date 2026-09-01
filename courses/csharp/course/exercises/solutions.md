# پاسخ مرجع تمرین‌ها

## cs-ex-fnd-002
```csharp
for (int i = 1; i <= 100; i++)
{
    if (i % 15 == 0) Console.WriteLine("AcademyCSharp");
    else if (i % 3 == 0) Console.WriteLine("Academy");
    else if (i % 5 == 0) Console.WriteLine("CSharp");
    else Console.WriteLine(i);
}
```

## cs-ex-fnd-003
```csharp
string customer = "Ali";
DateTime date = DateTime.Now;
decimal total = 12_000_000m;
Console.WriteLine($"{customer} | {date:yyyy/MM/dd} | {total:N0}");
```

## cs-ex-beg-001
```csharp
var sales = new List<decimal> { 100m, 250m, 90m, 400m };
Console.WriteLine($"Sum: {sales.Sum()}");
Console.WriteLine($"Average: {sales.Average()}");
Console.WriteLine($"Min: {sales.Min()}");
Console.WriteLine($"Max: {sales.Max()}");
```

## cs-ex-adv-002
```csharp
var gate = new SemaphoreSlim(3);
var tasks = items.Select(async item =>
{
    await gate.WaitAsync();
    try { await ProcessAsync(item); }
    finally { gate.Release(); }
});
await Task.WhenAll(tasks);
```

پاسخ‌ها مرجع هستند؛ روش‌های صحیح دیگری نیز ممکن است وجود داشته باشد.
