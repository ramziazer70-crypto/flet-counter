import flet as ft

def main(page: ft.Page):
    # إعدادات نافذة التطبيق الأساسية
    page.title = "تطبيقي الأول بـ Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # عنصر نصي لعرض الرقم (يبدأ بالرقم 0)
    number_text = ft.Text("0", size=50, weight=ft.FontWeight.BOLD)

    # دالة تُنفذ عند الضغط على زر الزيادة (+)
    def increment(e):
        number_text.value = str(int(number_text.value) + 1)
        number_text.update()

    # دالة تُنفذ عند الضغط على زر النقصان (-)
    def decrement(e):
        number_text.value = str(int(number_text.value) - 1)
        number_text.update()

    # إضافة العناصر إلى الشاشة (استخدمنا ft.Button بدلاً من ElevatedButton)
    page.add(
        ft.Row(
            [
                ft.Button("-", on_click=decrement),
                number_text,
                ft.Button("+", on_click=increment),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    )

# تشغيل التطبيق
ft.run(main)