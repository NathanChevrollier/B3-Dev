create Database ScoreIQ;
use ScoreIQ;

create table type_template(
    id_type int primary key auto_increment,
    type_name varchar(255) not null
);

create table question(
    id_question int primary key auto_increment,
    question_text varchar(255) not null,
    id_type int not null,
    foreign key (id_type) references type_template(id_type)
);

create table path_image(
    id_path_image int primary key auto_increment,
    path_image varchar(255) not null,
    id_type int not null,
    foreign key (id_type) references type_template(id_type)
);

