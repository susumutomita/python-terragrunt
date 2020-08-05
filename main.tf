data "template_file" "example" {
  template = "example1"
}


resource "local_file" "example" {
  content  = "${data.template_file.example.rendered} "
  filename = "example.txt"
}
