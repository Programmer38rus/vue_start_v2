<template>
  <div class="container">
    <div class="col-sm-10">
      <h1>Задачи</h1>
      <button type="button" id="task-add" class="btn btn-success btn-sm align-left d-block">
        Добавить задачу
      </button>
      <table class="table table-dark table-table-stripped table-hover">
        <thead class="thead-light">
          <tr>
            <th>Uid</th>
            <th>Описание</th>
            <th>Выполнена?</th>
            <th></th>
          </tr>
        </thead>

      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Todos',
};
</script>
